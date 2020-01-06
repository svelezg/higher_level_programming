#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -Ls "$1" -X DELETE