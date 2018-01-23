def lineChartHelper(dataTitle, data, label):
    out = {
        'labels':label,
        'datasets':[{
            'label': dataTitle,
            'data':data
        }]
    }
    return out

def TestGrafikLine(dataTitle, data, label):
    out = {
        'labels': label,
        'datasets' : [{
            'label' : dataTitle,
            'data'  : data
            
        }]
    }
    return out

def TestGrafikGender(dataTitle, data, label):
    out = {
        'labels': label,
        'datasets' : [{
            'label' : dataTitle,
            'data'  : data
            
        }]
    }
    return out

