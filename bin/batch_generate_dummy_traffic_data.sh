python3 -m src.filters._0_0_generate_dummy_traffic
python3 -m src.filters._0_1_preprocess_monthly_summary_for_traffic
sed -i '' 's/YearMonth/Trans_Date/g' workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Aggregated.csv
