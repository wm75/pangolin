KEY_ANALYSIS_MODE="analysis_mode"

KEY_QUERY_FASTA="query_fasta"
KEY_REFERENCE_FASTA="reference_fasta"

KEY_OUTDIR="outdir"
KEY_OUTFILE="outfile"

KEY_ALIGNDIR="aligndir"
KEY_ALIGNMENT_FILE="alignment_file"
KEY_ALIGNMENT_OUT="alignment_out"

KEY_TEMPDIR="tempdir"
KEY_NO_TEMP = "no_temp"

KEY_DATADIR="datadir"

KEY_MAXAMBIG="maxambig"
KEY_TRIM_START="trim_start"
KEY_TRIM_END="trim_end"

KEY_ALIAS_FILE="alias_file"

KEY_SKIP_SCORPIO = "skip_scorpio"

KEY_EXPANDED_LINEAGE="expanded_lineage"

KEY_USHER_PB = "usher_pb"
KEY_PLEARN_MODEL = "plearn_model"
KEY_PLEARN_HEADER = "plearn_header"
KEY_DESIGNATION_CACHE="designation_cache"
KEY_ASSIGNMENT_CACHE = "assignment_cache"
KEY_INPUT_COMPRESSION_TYPE = "compression_type"


# Version KEYS

KEY_PANGOLIN_DATA_VERSION="pangolin_data_version"
KEY_PANGOLIN_VERSION="pangolin_version"
KEY_CONSTELLATIONS_VERSION="constellations_version"
KEY_CONSTELLATIONS_PATH="constellations_path"
KEY_SCORPIO_VERSION="scorpio_version"
KEY_PANGOLIN_ASSIGNMENT_VERSION="pangolin_assignment_version"
KEY_PANGOLIN_ASSIGNMENT_PATH="pangolin_assignment_path"

KEY_VERBOSE="verbose"
KEY_LOG_API = "log_api"
KEY_THREADS="threads"

UNASSIGNED_LINEAGE_REPORTED="Unassigned"

# final report header
FINAL_HEADER= ["taxon", "lineage", "conflict", "ambiguity_score", 
"scorpio_call", "scorpio_support", "scorpio_conflict", "scorpio_notes", 
 "version", KEY_PANGOLIN_VERSION, KEY_SCORPIO_VERSION, KEY_CONSTELLATIONS_VERSION, 
"is_designated", "qc_status", "qc_notes", "note"]

HEADER_FIELD_MAP = {
    "name":"taxon",
    "scorpio_constellations":"scorpio_call",
    "designated":"is_designated",
    "usher_note":"note",
    "pangolearn_note":"note"

}

# File names 
DESIGNATION_CACHE_FILE = "lineages.hash.csv"
ALIAS_FILE = "alias_key.json"
USHER_ASSIGNMENT_CACHE_FILE = "usher_assignments.cache.csv.gz"

