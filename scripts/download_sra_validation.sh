#!/bin/bash
#SBATCH --job-name=sra_download
#SBATCH --output=sra_download_%j.out
#SBATCH --error=sra_download_%j.err
#SBATCH --time=24:00:00
#SBATCH --mem=8G
#SBATCH --cpus-per-task=4

# Download validation datasets from SRA for FRESH cervicotype project
# Usage: sbatch /path/to/download_sra_validation.sh
#
# Downloads 4 datasets:
#   1. Kyongo 2023 cpn60 (PRJNA898823) — 384 runs, Kenyan vaginal cpn60
#   2. Kwon FRESH 16S (PRJNA738803) — 29 runs, SA vaginal 16S
#   3. Albert 2015 cpn60 (PRJNA278895) — 310 runs, Canadian vaginal cpn60
#   4. Wuyts 2021 pheS (PRJNA629775) — 52 runs, pheS amplicon

set -euo pipefail

# Extract pipeline directory from SLURM job details
ORIGINAL_SCRIPT_PATH=$(scontrol show job $SLURM_JOB_ID | grep -oP 'Command=\K[^ ]+')
PIPELINE_DIR="$(dirname "$ORIGINAL_SCRIPT_PATH")"

# Paths
DATA_DIR="/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/validation/public_data"
SCRATCH_DIR="/scratch/sahlab/kathie/fresh_cervicotype_analysis/sra_downloads"
RUN_DIR="${DATA_DIR}"

# Activate conda with SRA tools
source /ref/sahlab/software/anaconda3/bin/activate
conda activate /ref/sahlab/software/sra-tools-env

# Create output directories
mkdir -p "${DATA_DIR}/kyongo_2023_cpn60"
mkdir -p "${DATA_DIR}/gosmann_kwon_16S"
mkdir -p "${DATA_DIR}/albert_2015_cpn60"
mkdir -p "${DATA_DIR}/wuyts_2021_pheS"
mkdir -p "${SCRATCH_DIR}"

echo "$(date): Starting SRA downloads"
echo "fasterq-dump version: $(fasterq-dump --version 2>&1 | head -1)"

# Function to download a dataset
download_dataset() {
    local NAME=$1
    local RUN_FILE=$2
    local OUT_DIR=$3
    local NUM_RUNS=$(wc -l < "$RUN_FILE")

    echo ""
    echo "=========================================="
    echo "$(date): Downloading ${NAME} (${NUM_RUNS} runs)"
    echo "  Run file: ${RUN_FILE}"
    echo "  Output: ${OUT_DIR}"
    echo "=========================================="

    local COUNT=0
    local FAILED=0
    while IFS= read -r SRR; do
        COUNT=$((COUNT + 1))
        # Skip if already downloaded
        if [ -f "${OUT_DIR}/${SRR}_1.fastq.gz" ] || [ -f "${OUT_DIR}/${SRR}.fastq.gz" ]; then
            echo "  [${COUNT}/${NUM_RUNS}] ${SRR} — already exists, skipping"
            continue
        fi

        echo "  [${COUNT}/${NUM_RUNS}] ${SRR} — downloading..."
        if fasterq-dump --split-files --threads 4 --temp "${SCRATCH_DIR}" \
            --outdir "${OUT_DIR}" "${SRR}" 2>/dev/null; then
            # Compress
            gzip -f "${OUT_DIR}/${SRR}"*.fastq 2>/dev/null
            echo "    OK"
        else
            echo "    FAILED: ${SRR}" >> "${OUT_DIR}/failed_downloads.txt"
            FAILED=$((FAILED + 1))
            echo "    FAILED"
        fi

        # Rate limit: brief pause between downloads
        sleep 1
    done < "$RUN_FILE"

    echo "$(date): ${NAME} complete — ${COUNT} attempted, ${FAILED} failed"
}

# Download each dataset
# Priority 1: Kyongo cpn60 (African cpn60 validation)
download_dataset "Kyongo_2023_cpn60" \
    "${RUN_DIR}/PRJNA898823_runs.txt" \
    "${DATA_DIR}/kyongo_2023_cpn60"

# Priority 2: FRESH/Kwon 16S (baseline comparison)
download_dataset "Gosmann_Kwon_16S" \
    "${RUN_DIR}/PRJNA738803_runs.txt" \
    "${DATA_DIR}/gosmann_kwon_16S"

# Priority 3: Albert cpn60 (Western cpn60 validation)
download_dataset "Albert_2015_cpn60" \
    "${RUN_DIR}/PRJNA278895_runs.txt" \
    "${DATA_DIR}/albert_2015_cpn60"

# Priority 4: Wuyts pheS (pheS classifier validation)
download_dataset "Wuyts_2021_pheS" \
    "${RUN_DIR}/PRJNA629775_runs.txt" \
    "${DATA_DIR}/wuyts_2021_pheS"

echo ""
echo "$(date): All downloads complete"
echo "Output directory: ${DATA_DIR}"
ls -lh "${DATA_DIR}"/*/
