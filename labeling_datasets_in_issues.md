# Labeling Format for Datasets/Issues
This has been the approach so far when labeling.

## Status Labels
*Objective*: Status labels are designed to help mirror owners determine which labels need mirroring - these are probably the most important labels in helping people contribute. In general, the long-term goal
would be to have more than one mirror of each of these datasets, and the status labels indicate how many mirrors exist. In this category, we have the following labels:

 * _Status: No Mirrors_: We do not know of any available mirrors for this data
 * _Status: Offline Mirror_: We have reports of an offline mirror for this data, but no URL exists for accessing it. This is its own label because it's less reliable than an online mirror in that it can't be verified.
 * _Status: One Mirror_: We know of at least one online mirror with a URL.
 * _Status: Two or More Mirrors_: We know of at least two online mirrors with URLs.
 
Ideally, marking any of the status labels except _Status: No Mirrors_ is accompanied by a link or other documentation about where that mirror is located. When the datasets list was imported to GitHub issues, the code that imported marked _Status: One Mirror_ for any dataset previously marked as complete, but that doesn't mean the mirror is *known* yet, so we should look out for any that have this label without a mirror. Some may need to be transitioned to _Status: Offline Mirror_.

## Mirror Labels
*Objective*: Labels prefixed with _Mirror_ are designed to help people filter by mirror quality, in order to determine if the dataset needs more mirrors.

 * _Mirror: Internet Archive_: Dataset is mirrored at the Internet Archive. Highest quality archive, but accessibility varies based on whether the data was a directory, or a website
 * _Mirror: Private_: A publicly available mirror has been created online, but it is hosted on privately owned or rented servers (other than those of the Internet Archive). A URL should be provided in the issue for it to have this label.
 * _Mirror: Verified_: Not yet in use, but designed to be used for cross verification by third parties that a dataset is complete and accurate compared with source. IPFS copies meet this criteria by default, but no known mirrors use that yet.
 
## Type Labels
*Objective*: Type labels are designed to help people filter by what technology/expertise is required in order to mirror a dataset/

 * _Type: Bulk Downloadable_:
 * _Type: Requires Contacting Agency_:
 * _Type: Requires Crawling_:
 
## Priority Labels

## Other labels
