from os import system, name, makedirs
import time
import re
import pyfiglet
import requests
import yagooglesearch

''' 
    Clear the screen
'''
def clear()->None: system('cls') if name == 'nt' else system('clear')

''' 
    Validate a domain name against a regex
    @param domain: domain name to validate
    @return: True if valid, False if not
'''
def validDomainName(domain:str)->bool:
    return re.match('''
        (?=^.{,253}$)          # max. length 253 chars
        (?!^.+\.\d+$)          # TLD is not fully numerical
        (?=^[^-.].+[^-.]$)     # doesn't start/end with '-' or '.'
        (?!^.+(\.-|-\.).+$)    # levels don't start/end with '-'
        (?:[a-z\d-]            # uses only allowed chars
        {1,63}(\.|$))          # max. level length 63 chars
        {2,127}                # max. 127 levels
        ''', domain, re.X | re.I)

'''
    Ask the user for a valid integer option
    @param min: minimum value for the option
    @param max: maximum value for the option
    @return: the integer option
'''
def getOption(min:int,max:int)->int:
    option = min -1
    while option>max or option<min:
        option = int(input("Indica l'opció desitjada (%d,%d): "%(min,max)))
    return option

''' 
    Ask the user for a valid domain name
    @return: the domain name
'''
def getDomain()->str:
    domain = input("Indica el domini desitjat: ")
    domain='.'.join(domain.casefold().split('.')[-2:])
    while not validDomainName(domain):
        print("El domini no és vàlid, recorda que cal indicar-lo sense subdominis")
        domain = input("Indica el domini desitjat: ")
        domain='.'.join(domain.casefold().split('.')[-2:])
    return domain

''' 
    Use yagooglesearch to get search results for a specific query
    @param query: the query to search
    @param verbose: the verbosity level for yagooglesearch
    @param allInfo: if True, show all the info for each result
    @param max: the maximum number of results to get
    @return: a list of results
'''
def doGoogleSearch(query:str,verbose:int=1,allInfo:bool=False,max:int=100)->list:
    print(f'Dork: "{query}"')
    client = yagooglesearch.SearchClient(
            query,
            tbs="li:1",
            max_search_result_urls_to_return=max,
            http_429_cool_off_time_in_minutes=45,
            http_429_cool_off_factor=1.5,
            #proxy="socks5h://127.0.0.1:9050",
            #verbosity=5,
            verbosity=verbose,
            verbose_output=allInfo,  # False (only URLs) or True (rank, title, description, and URL)
        )
    client.assign_random_user_agent()
    print('Realitzant Cerca a Google...')
    results=client.search()
    print(f'Obtinguts {len(results)} resultats possibles')
    return results

''' 
    Get all the files from a domain
    @param domain: the domain name
'''
def getAllFiles(domini:str)->None:
    pass
    #TODO: Implement dork search for getting files from an specific domain (parse URLs required), storing results in binary file'''
    ''' Code for downloading a file from an URL and storing them in a binary file, using requests library
        r = requests.get(url)
        if r.status_code==200:
            fileName=url.split('/')[-1]
            with open(fileName,'wb') as file:
                file.write(r.content)
    '''
''' 
    Get all the emails from a domain
    @param domain: the domain name
'''
def getAllEmails(domini:str)->None:
    pass
    #TODO: Implement dork search for getting emails from an specific domain (parse URLs description required), storing results in text file'''

''' 
    Get all the subdomains from a domain
    @param domain: the domain name
'''
def getAllSubdomains(domini:str)->None:
    pass
    #TODO: Implement dork search for getting subdomains from an specific domain (parse URLs required), storing results in text file'''

''' 
    Get all the results from a custom dork entered by the user
'''
def doCustomDork()->None:
    pass
    #TODO: Implement custom dork search, storing results in a CSV file with format: rank, url, title, description'''

''' 
    Show Credits
'''
def showTitle()->None:
    ASCII_art_1 = pyfiglet.figlet_format("DorkPy",font='standard')
    ASCII_art_2 = pyfiglet.figlet_format("by XXXX XXX",font='digital')
    print(ASCII_art_1)
    print(ASCII_art_2)

''' 
    Show Main menu
'''
def showMenu()->None:
    print()
    print("1) Obtenir fitxers")
    print("2) Obtenir emails")
    print("3) Obtenir subdominis (exc. www)")
    print("4) Utilitzar un Dork personalitzat")
    #TODO: Add more interesting options to increase your mark
    print()

''' 
    Main function
'''
def main():
    clear()
    showTitle()
    showMenu()
    opcio=getOption(1, 4)
    if opcio == 1:
        domini=getDomain()
        getAllFiles(domini)
    elif opcio == 2:
        domini=getDomain()
        getAllEmails(domini)
    elif opcio == 3:
        domini=getDomain()
        getAllSubdomains(domini)
    elif opcio == 4:
        doCustomDork()

    print("\nRecords al Maese LeGon!")


if __name__ == "__main__":
    main()
