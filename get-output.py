import sys
import xml.dom.minidom
from sickle import Sickle

ENDPOINT = 'https://durham-repository.worktribe.com/oaiprovider'
sickle = Sickle(ENDPOINT)

prefix = 'oai:durham-repository.worktribe.com:'
TESTID = '1168839'


def get_rioxx(repo_id):
    id = prefix + repo_id
    r = sickle.GetRecord(identifier=id, metadataPrefix='rioxx')
    dom = xml.dom.minidom.parseString(str(r))
    pretty = dom.toprettyxml()
    print(pretty)

def get_dc(repo_id):
    id = prefix + repo_id
    r = sickle.GetRecord(identifier=id, metadataPrefix='oai_dc')
    dom = xml.dom.minidom.parseString(str(r))
    pretty = dom.toprettyxml()
    print(pretty)

def main():
    print("rioxx format")
    get_rioxx(sys.argv[1])
    print("\n***************************************************\n")
    print("Dublin Core format")
    get_dc(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main())  #
