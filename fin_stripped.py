full_dict = {
'148' : 'alphaABCupHIKWdown',
'113' : 'alphagammabetadeltaACupDEFGKdownPrDEFRs',
'163' : 'alphaFACupTGWdownIW',
'162' : 'alphaDEFAACBupHIHIKKdownW',
'151' : 'alphaABCupHIKdown',
'152' : 'alphaAupHIKdown',
'154' : 'upDEFTGACupFHIKW',
'131' : 'alphaABCupHIKdownW',
'108' : 'alphagammabetazetaetathetaAupDEdownPrRsPrRs',
'145' : 'alphaABCFupGKdown',
'135' : 'alphaACFHIKdownPrRsPrRs',
'149' : 'ABCupHIdownIKW',
'114' : 'alphaADEFPrRsupDEdownFPrRsOQW',
'127' : 'alphaAOFKTPrRsQExUW',
'140' : 'alphagammadeltabetaABCupDEGFIKdownW'
}

prepless_dict = {
'148' : 'ABCupHIKWdown',
'113' : 'ACupDEFGKdownPrDEFRs',
'163' : 'FACupTGWdownIW',
'162' : 'DEFAACBupHIHIKKdownW',
'151' : 'ABCupHIKdown',
'152' : 'AupHIKdown',
'154' : 'upDEFTGACupFHIKW',
'131' : 'ABCupHIKdownW',
'108' : 'AupDEdownPrRsPrRs',
'145' : 'ABCFupGKdown',
'135' : 'ACFHIKdownPrRsPrRs',
'149' : 'ABCupHIdownIKW',
'114' : 'ADEFPrRsupDEdownFPrRsOQW',
'127' : 'AOFKTPrRsQExUW',
'140' : 'ABCupDEGFIKdownW'
}


strings = [full_dict, prepless_dict]

def parse_grams():
    # for each dict in strings list, for each item in the dict
    for elem in strings:
        for k,v in elem.items():
            # for each grammar in the list, try parsing
            print(k + v)

