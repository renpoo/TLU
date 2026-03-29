bash bin/orchestrators/0_0_run_dummy_generator.sh
python3 -m src.filters._0_0_preprocess_journal
python3 src/filters/_0_1_preprocess_monthly_summary.py < workspace/input_stream/Dummy_Journal_Stream_Amount.csv > workspace/input_stream/Dummy_Journal_Stream_Amount.Monthly.csv
bash bin/batch_unittest.sh
bash bin/batch_processing.sh
bash bin/batch_visualize_graphs.sh
