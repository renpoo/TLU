export TARGET_ENV=${TARGET_ENV:-"workspace"}
mkdir -p "${TARGET_ENV}/ephemeral"
python3 -m src.filters._0_0_generate_dummy_traffic --out-initial-state "${TARGET_ENV}/ephemeral/_initial_state_labels.csv" > "${TARGET_ENV}/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv"
python3 -m src.filters._0_1_preprocess_monthly_summary_for_traffic
