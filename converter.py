def covert(df, drop, rename, inflow_source):
    print(df)
    result = df.copy()

    outflow = []
    inflow = []
    for _, row in df.iterrows():
        if row.get(inflow_source) >= 0:
            inflow.append(row.get(inflow_source))
            outflow.append(0)
        else:
            inflow.append(0)
            outflow.append(abs(row.get(inflow_source)))
    result['Outflow'] = outflow
    result['Inflow'] = inflow

    result.drop(columns=drop, inplace=True)
    result.rename(columns=rename, inplace=True)

    print(result)

    return result