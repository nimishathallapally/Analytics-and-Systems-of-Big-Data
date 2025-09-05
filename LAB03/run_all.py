# run_all.py
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import subprocess

# --- Utility: Save CSV as Image ---
def save_csv_as_image(csv_path, img_path, figsize=(6, 4)):
    df = pd.read_csv(csv_path)
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis('off')
    tbl = pd.plotting.table(ax, df, loc='center', cellLoc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1.2, 1.2)
    plt.savefig(img_path, bbox_inches='tight')
    plt.close()

# --- Questions and Folders ---
questions = {
    "Q1_histogram": "q1_histogram.py",
    "Q2_stem_leaf": "q2_stem_leaf.py",
    "Q3_density": "q3_density.py",
    "Q4_scatter": "q4_scatter.py",
    "Q5_box_swarm": "q5_box_swarm.py",
    "Q6_violin": "q6_violin.py",
    "Q7_radar": "q7_radar.py",
    "Q8_funnel": "q8_funnel.py",
    "Q9_correlation": "q9_correlation.py",
}

# --- Loop through all questions ---
for folder, script in questions.items():
    q_dir = os.path.join(os.getcwd(), folder)
    script_path = os.path.join(q_dir, script)

    if not os.path.exists(q_dir):
        print(f"⚠️ Skipping {folder}, directory not found.")
        continue

    if not os.path.exists(script_path):
        print(f"⚠️ Skipping {script}, not found in {q_dir}.")
        continue

    # Run script inside its folder
    print(f"▶️ Running {script} in {folder} ...")
    subprocess.run(["python3", script], cwd=q_dir)

    # Convert CSV → PNG table
    for file in os.listdir(q_dir):
        if file.endswith(".csv"):
            csv_path = os.path.join(q_dir, file)
            img_path = os.path.join(q_dir, file.replace(".csv", "_table.png"))
            save_csv_as_image(csv_path, img_path)

print("\n✅ All questions executed. Graphs, CSVs, and table images saved inside each Q-folder.")