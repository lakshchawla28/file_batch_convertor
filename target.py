def available_targets(ext):
    mapping={
        ".csv":[(".json","JSON"),(".xlsx","Excel")],
        ".json":[(".csv","CSV"),(".xlsx","Excel")],
        ".xlsx":[(".json","JSON"),(".csv","CSV")],
       
    }
    return mapping.get(ext.lower(),[])

        
