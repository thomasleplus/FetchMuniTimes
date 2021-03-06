# FetchMuniTimes

Deployment package for an AWS Lamba returning the next times at a selection of stations.

[![Flake8](https://github.com/thomasleplus/FetchMuniTimes/workflows/Flake8/badge.svg)](https://github.com/thomasleplus/FetchMuniTimes/actions?query=workflow:"Flake8")
[![CodeQL](https://github.com/thomasleplus/FetchMuniTimes/workflows/CodeQL/badge.svg)](https://github.com/thomasleplus/FetchMuniTimes/actions?query=workflow:"CodeQL")

This Python Lambda can be mapped to an AWS API Gateway GET Resource with 3 URL parameters:
* uuid: the UUID of a Transit Tracker created at https://511.org/transit/tracker/overview beforehand
* min: the minimum time to display (in minutes, default is 0)
* max: the maximum time to display (in minutes, default is 99)
