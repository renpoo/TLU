ENV_DIR="${TARGET_ENV:-workspace}"

bash bin/orchestrators/0_0_run_dummy_generator.sh
# Note: 0_0_preprocess_journal internally uses ENV_DIR or hardcodes workspace? Let's assume it reads the same file.
# Wait, _0_0_preprocess_journal.py probably has hardcoded paths! We'll pass the files via stdin/stdout or fix it.
# It's better to just pass the right paths. Let's fix this in the script.
python3 -m src.filters._0_0_preprocess_journal "${ENV_DIR}/input_stream/Dummy_Journal_Stream.csv" "${ENV_DIR}/input_stream/Dummy_Journal_Stream_Amount.csv"
python3 -m src.filters._0_1_preprocess_weekly_summary < "${ENV_DIR}/input_stream/Dummy_Journal_Stream_Amount.csv" > "${ENV_DIR}/input_stream/Dummy_Journal_Stream_Amount.Aggregated.csv"
