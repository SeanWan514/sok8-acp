#!/usr/bin/env python3
"""Exact Case A thresholds, independent payoff checks, and parameter-wide figure.

Run with Python, NumPy, Matplotlib, SymPy, and PyYAML. No service/API calls.
The figure uses the zero-fee submodel and sweeps the entire dimensionless domain.
"""
from pathlib import Path
import csv
import hashlib
import json
import platform
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.text import Text
import numpy as np
import sympy as sp
import yaml

ROOT = Path(__file__).resolve().parent


def verify():
    t, b, d, e, k, q = sp.symbols("theta b d eta kappa q", positive=True)
    qa = (2*d*(t+b)-d**2+e)/(t*(t+2*b))
    qp = 1-((t-d)**2-k)/t**2
    agent_gain = (d-t-b)**2-q*b**2-(1-q)*(t+b)**2-e
    user_gain = (d-t)**2-k-(1-q)*t**2
    gap = (2*b*d*(t-d)+(t+2*b)*k-t*e)/(t**2*(t+2*b))
    assert sp.simplify(agent_gain-t*(t+2*b)*(q-qa)) == 0
    assert sp.simplify(user_gain-t**2*(q-qp)) == 0
    assert sp.simplify(qp-qa-gap) == 0
    x, z = sp.symbols("x z", positive=True)
    normalized = {d:x*t, b:z*t/(2*(1-z)), e:0, k:0}
    assert sp.simplify((qp-qa).subs(normalized)-z*x*(1-x)) == 0
    assert sp.simplify(qa.subs(normalized)-(2*x-x**2-z*x*(1-x))) == 0

    # Independent direct evaluation of the two actions across positive costs,
    # varying scales and binding/non-binding caps. Values are verification
    # inputs, not empirical observations or the data shown in the figure.
    rng = np.random.default_rng(20261013)
    n = 100000
    tv = 10.0**rng.uniform(-2, 2, n)
    bv = tv*10.0**rng.uniform(-3, 2, n)
    dv = (tv+bv)*rng.uniform(0, 1.5, n)
    ev = tv**2*rng.uniform(0, 2, n)
    kv = tv**2*rng.uniform(0, 2, n)
    qv = rng.uniform(0, 1, n)
    a = np.minimum(tv+bv, dv)
    va = -(a-tv-bv)**2
    vr = -qv*bv**2-(1-qv)*(tv+bv)**2-ev
    la = (a-tv)**2
    lr = kv+(1-qv)*tv**2
    qav = (2*dv*(tv+bv)-dv**2+ev)/(tv*(tv+2*bv))
    qpv = 1-((tv-dv)**2-kv)/tv**2
    binding = dv < tv+bv
    assert np.array_equal(vr[binding] > va[binding], qv[binding] > qav[binding])
    assert np.array_equal(lr[binding] < la[binding], qv[binding] > qpv[binding])
    assert not np.any(vr[~binding] > va[~binding])
    harmful = (vr > va) & (lr > la)
    predicted = binding & (qv > qav) & (qv < qpv)
    assert np.array_equal(harmful, predicted)
    # For any fixed cap and zero user fee, fallback to the autonomous action
    # weakly improves user loss whenever review is requested.
    fallback_loss = (1-qv)*la
    assert np.all(fallback_loss <= la)
    for beta in [0, 1e-6, .01, .1, 1, 100, 10000]:
        xx = np.linspace(0, 1, 1001)
        qaa = (2*xx*(1+beta)-xx**2)/(1+2*beta)
        qpp = 2*xx-xx**2
        assert np.all(qaa >= xx-1e-12)
        assert np.all(qpp >= qaa-1e-12)
        if beta == 0:
            assert np.allclose(qaa, qpp)
        else:
            midpoint = (qaa[1:-1]+qpp[1:-1])/2
            vaa = -(xx[1:-1]-1-beta)**2
            vrr = -midpoint*beta**2-(1-midpoint)*(1+beta)**2
            assert np.all(vrr > vaa)
            assert np.all(1-midpoint > (1-xx[1:-1])**2)
    return {
        "symbolic_identities": 5,
        "direct_payoff_checks": n,
        "seed": 20261013,
        "checks": ["agent threshold", "user threshold", "non-binding cap",
                   "harmful-review interval", "zero-bias boundary",
                   "positive-bias zero-fee interval", "autonomous fallback"],
        "all_passed": True,
    }


def plot(output):
    output.mkdir(parents=True, exist_ok=True)
    theme = yaml.safe_load((ROOT/"theme.yaml").read_text())
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9,
        "axes.labelsize": 10, "axes.titlesize": 11,
        "xtick.labelsize": 9, "ytick.labelsize": 9,
        "legend.fontsize": 9, "pdf.fonttype": 42,
        "svg.fonttype": "none", "svg.hashsalt": "sok8-acp-case-a", "axes.linewidth": .8,
        "text.color": "#18324A", "axes.labelcolor": "#18324A",
        "axes.edgecolor": "#18324A", "savefig.facecolor": "white",
    })
    xx = np.linspace(0, 1, 201)
    zz = np.linspace(0, 1, 201)
    X, Z = np.meshgrid(xx, zz)
    QP = 2*X-X*X
    GAP = Z*X*(1-X)
    QA = QP-GAP
    with (output/"threshold-surface.csv").open("w", newline="") as f:
        out = csv.writer(f)
        out.writerow(["cap_ratio_x", "bias_index_z", "q_agent", "q_user", "harmful_interval_width", "bias_limit"])
        out.writerows(zip(X.ravel(), Z.ravel(), QA.ravel(), QP.ravel(), GAP.ravel(), (Z==1).ravel()))

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(7, 2.95))
    fig.subplots_adjust(left=.09, right=.92, bottom=.20, top=.88, wspace=.50)
    burgundy = "#a30543"
    ax.fill_between(xx, 0, xx, color="#f2f3f5")
    ax.fill_between(xx, xx, 2*xx-xx*xx, facecolor="#f9e8ee", edgecolor=burgundy, hatch="///", linewidth=0)
    ax.fill_between(xx, 2*xx-xx*xx, 1, color="#80cba4", alpha=.35)
    ax.plot(xx, 2*xx-xx*xx, color=burgundy, linewidth=1.8)
    ax.plot(xx, xx, color="#59616a", linestyle="--", linewidth=1.5)
    ax.text(.05, .92, "Review benefits user", fontsize=9)
    ax.text(.40, .60, "Harm possible", fontsize=9, color=burgundy,
            rotation=31, ha="center", va="center", bbox=dict(facecolor="#f9e8ee", edgecolor="none", pad=.7))
    ax.text(.63, .22, "No review", fontsize=9, ha="center")
    ax.text(.77, .965, r"$q_P$", fontsize=10, color=burgundy, ha="center")
    ax.text(.82, .68, r"$q_A\to x$", fontsize=9, rotation=39, color="#59616a", ha="center")
    ax.set_title("(a) Decision regions", loc="left")
    ax.set_xlabel(r"Relative cap, $x=d/\theta$")
    ax.set_ylabel(r"Timely review, $q$")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([0, .25, .5, .75, 1]); ax.set_yticks([0, .25, .5, .75, 1])

    cmap = LinearSegmentedColormap.from_list("harm", ["#ffffff", "#f3cbd9", burgundy])
    hm = bx.pcolormesh(X, Z, GAP, cmap=cmap, vmin=0, vmax=.25, shading="auto", rasterized=True)
    contours = bx.contour(X, Z, GAP, levels=[.05, .10, .15, .20], colors="#59616a", linewidths=.65)
    bx.clabel(contours, inline=True, fontsize=8.5, fmt="%.2f",
              manual=[(.17,.355),(.25,.533),(.38,.637),(.50,.80)])
    bx.set_title("(b) Harmful interval width", loc="left")
    bx.set_xlabel(r"Relative cap, $x=d/\theta$")
    bx.set_ylabel(r"Relative bias, $z$")
    bx.set_xlim(0, 1); bx.set_ylim(0, 1)
    bx.set_xticks([0, .25, .5, .75, 1]); bx.set_yticks([0, .25, .5, .75, 1])
    bx.set_yticklabels(["0", ".25", ".50", ".75", "1 (limit)"])
    cb = fig.colorbar(hm, ax=bx, fraction=.055, pad=.04, ticks=[0, .05, .10, .15, .20, .25])
    cb.ax.tick_params(labelsize=9)
    for a in (ax, bx):
        a.spines[["top", "right"]].set_visible(False)
        a.tick_params(length=3)
    fig.canvas.draw()
    texts = [a for a in fig.findobj(match=lambda a:isinstance(a,Text)) if a.get_visible() and a.get_text().strip()]
    minimum = min(a.get_fontsize() for a in texts)
    assert minimum >= 8
    # Keep physical dimensions fixed: no tight crop that would rescale fonts.
    for ext in ["pdf", "svg", "png"]:
        metadata = {"CreationDate": None, "ModDate": None} if ext == "pdf" else {"Date": None} if ext == "svg" else {}
        fig.savefig(output/f"case-a-threshold-regions.{ext}", dpi=300, metadata=metadata)
    plt.close(fig)
    return {"theme": theme, "figure_width_in": 7, "minimum_text_pt": minimum,
            "analytic_surface_rows": int(X.size), "numerical_uncertainty": "none; deterministic formulas",
            "domain": "0<=x<=1, 0<=z<1; z=1 is the infinite-bias limit",
            "fees": "eta=kappa=0; general nonzero-cost thresholds remain symbolic in the manuscript",
            "columns": "q_A=2x-x^2-zx(1-x); q_P=2x-x^2; width=z x(1-x)"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT)
    args = parser.parse_args()
    result = {"verification": verify(), "figure": plot(args.output),
              "versions": {"python":platform.python_version(), "numpy":np.__version__,
                           "matplotlib":matplotlib.__version__, "sympy":sp.__version__}}
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (args.output/"validation.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
