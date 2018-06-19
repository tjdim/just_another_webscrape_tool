"""Get, save and parse content from url """
#tjdim, Cambridge MA 2018
import re
import urllib2
from bs4 import BeautifulSoup
from _file_org import _save_dat_to_file
def _built_url(search_engine, keyword):
    """Creates url from search engine url and keyword
       Args
       ----
           search_engine (str) : url of search engine
           keyword (str) :  keyword(s) to search

       Returns
       -------
            url (str) : url (search engine plus keywords) in search engine format

       Example
       -------
            >>> built_url('', 'example')
    """
    if not search_engine:
        #Enter default search engine here
        search_engine = ''
    try:
        #built url
        url = search_engine + re.sub("\s+", "+", keyword.strip())
        print "Builts URL " + url
        return url
    except Exception, error:
        print "Error message: " + str(error)


def _get_content_from_url(url):
    """ Call url and get content.

        Args
        ----
            url (str) : url link

        Returns
        -------
            url_content (str) : html code
    """
    #Enter user agent here!
    uagent = ' '
    modified_header = {}
    #replace user agent
    modified_header['User-Agent'] = uagent
    request = urllib2.Request(url, headers=modified_header)
    try:
        url_response = urllib2.urlopen(request)
        url_content = url_response.read()
        return url_content
    except Exception, error:
        print str(error)


def _parse_content(url_data, tag_name, class_name, nested_search=True):
    """Parses content from url UNDER CONSTRUCTION
       Args
       ----
       url_data (str) : html data to parse
       tag_name (array(str)) : tag which you like to parse, e.g 'div', 'h1'
       class_name (array(str)) : class name of tag to parse
       nested_search (boolean) : default value true
    """
    #url data to BS format
    parse_data = BeautifulSoup(url_data, 'html.parser')
    if class_name[0] == '':
        pass
    else:
        parse_data = parse_data.find_all(re.compile(tag_name[0]), attrs={'class': class_name[0]})
    collected_data = []
    #for nested search
    print '--------------parsing in progress-------------------'
    try:
        if nested_search:
            for subsub_tag in parse_data:
                listitem = subsub_tag.find(re.compile(tag_name[1]), attrs={'class': class_name[1]})
                if listitem:
                    collected_data.append(listitem.text)
    except Exception, error:
        print " Nested search is disabled. Error message: " + str(error)
        for sub_tag in parse_data:
            #print sub_tag
            collected_data.append(sub_tag.text.strip().encode('ascii', 'ignore'))
    print '--------------parsing finished-------------------'
    return collected_data


def _content(search_engine, keyword, input_url, tag_name, class_name):
    """Get html content from input url or from search engine keyword search.
        Save parsed data to file.

        Args
        ----
            search_engine (str) : url of search engine
            keyword (str)       : keyword(s) to search
            input_url (str)     : input url or search_engine
            tag_name (str)     : tag to search
            class_name (str)     : class to search


        Calls
        -----
            _built_url
            _get_content_from_url
            _parse_content
            _save_dat_to_file

        Returns
        -------
             txt-file with raw data (html content)
             txt-file with parsed html content
    """
    if input_url == '':
        url = _built_url(search_engine, keyword)
        print 'Parsing ' + url
    else:
        url = input_url
        print 'Parsing ' + url
    return_data = _get_content_from_url(url)
    parsed_data = _parse_content(return_data, tag_name, class_name)
    if input_url == '':
        _save_dat_to_file(keyword, parsed_data)
        print 'End search for keyword: ' + keyword
    else:
       #extract keyword inbetween points www.keyword.de
        keyword = input_url.split('.')[1]
        print keyword
        _save_dat_to_file(keyword, parsed_data)
