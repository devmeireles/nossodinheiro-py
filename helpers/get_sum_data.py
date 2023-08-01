from helpers.format_to_millions import format_to_millions


def get_sum_data(dataframe, groupCol, tupleCol, resetIndexName, sortValues):
    grouped_data = dataframe.groupby(groupCol)[tupleCol].sum()
    top_suppliers_df = grouped_data.reset_index(
        name=resetIndexName).sort_values(by=sortValues, ascending=False)

    top_suppliers_df[resetIndexName] = top_suppliers_df[resetIndexName].apply(
        format_to_millions)

    return top_suppliers_df
