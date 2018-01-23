def HelpersPenclub(label, data):
    out = {
        'labels': label,
        'datasets' : [{
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