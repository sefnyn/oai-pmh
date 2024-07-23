# oai-pmh 🐄

## Endpoint
https://durham-repository.worktribe.com/oaiprovider

## Requirements

###
pip install **pyoai**  
pip install **sickle**

## Usage:
**get-output.py** WorktribeOutputID  # get one output in two metadata formats

## Output
Two files:  
dc.xml  
rioxx.xml

**ck-rioxx.py** FileContainingWorktribeOutputIDs  # check input file for RIOXX 2.0 compliance

## Output
logfile.log  
rioxx.xml

**fileck.py** FileContainingWorktribeOutputIDs  # check for records with multiple files in <dc:identifier>

## Output
Total outputs analysed: x   
Outputs with multiple files: y   

**get-doi.py** FileContainingWorktribeOutputIDs  # look for Worktribe records containing DOIs

## Output
Total outputs analysed:  77,648  
Outputs with a DOI:  49,122   
[Creates file doi.txt]
