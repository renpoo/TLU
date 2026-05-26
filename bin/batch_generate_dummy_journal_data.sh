ENV_DIR="${TARGET_ENV:-workspace}"

bash bin/orchestrators/0_0_run_dummy_generator.sh
bash bin/orchestrators/00_0_run_preprocess_journal.sh "month"
