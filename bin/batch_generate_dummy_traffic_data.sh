export TARGET_ENV=${TARGET_ENV:-"workspace"}
mkdir -p "${TARGET_ENV}/ephemeral"
python3 -m src.filters._0_0_generate_dummy_traffic --out-initial-state "${TARGET_ENV}/ephemeral/_initial_state_labels.csv" \
| python3 -m src.filters._0_1_aggregate_stream \
    --col_time "Trans_Date" --col_src "Src" --col_tgt "Tgt" --col_val "Amount" \
    --interval "month" \
> "${TARGET_ENV}/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv"
