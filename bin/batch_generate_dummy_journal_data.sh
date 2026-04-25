bash bin/orchestrators/0_0_run_dummy_generator.sh
python3 -m src.filters._0_0_preprocess_journal
python3 -m src.filters._0_1_preprocess_monthly_summary < workspace/input_stream/Dummy_Journal_Stream_Amount.csv > workspace/input_stream/Dummy_Journal_Stream_Amount.Aggregated.csv
# python3 -m src.filters._0_1_preprocess_quaterly_summary < workspace/input_stream/Dummy_Journal_Stream_Amount.csv > workspace/input_stream/Dummy_Journal_Stream_Amount.Aggregated.csv
