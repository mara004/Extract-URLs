# Input: repo_urls.json
# Output: file_url_counts.csv (file name, URL count, category) and ecdf_number.csv (URLCount, ecdf, category)
# Notes: 

import json
import csv
from statsmodels.distributions.empirical_distribution import ECDF

repo_file = open("./repo_results/repo_urls.json")
repo_json = json.load(repo_file)
repo_file.close()

csv_file = open("./data_processing/file_url_counts.csv", "w")
csvwriter = csv.writer(csv_file)
csvwriter.writerow(['Filename', 'URLCount', 'Category'])

csv_file2 = open("./data_processing/ecdf_numbers.csv", "w")
csvwriter2 = csv.writer(csv_file2)
csvwriter2.writerow(['URLCount', 'ecdf', 'Category'])

sf = []
gh = []
gl = []
bb = []

for dir in repo_json:
    for file in repo_json[dir]["files"]:
        try:
            sourceforge_count = repo_json[dir]["files"][file]["sourceforge"]["url_count"]
            csvwriter.writerow([file, sourceforge_count, "SourceForge"])
            sf.append(sourceforge_count)
        except:
            pass
        try:
            github_count = repo_json[dir]["files"][file]["github"]["url_count"]
            csvwriter.writerow([file, github_count, "GitHub"])
            gh.append(github_count)
        except:
            pass
        try:
            gitlab_count = repo_json[dir]["files"][file]["gitlab"]["url_count"]
            csvwriter.writerow([file, gitlab_count, "GitLab"])
            gl.append(gitlab_count)
        except:
            pass
        try:
            bitbucket_count = repo_json[dir]["files"][file]["bitbucket"]["url_count"]
            csvwriter.writerow([file, bitbucket_count, "Bitbucket"])
            bb.append(bitbucket_count)
        except:
            pass

sf_ecdf = ECDF(sf)
gh_ecdf = ECDF(gh)
gl_ecdf = ECDF(gl)
bb_ecdf = ECDF(bb)

for i in range(len(sf_ecdf.x)):
    csvwriter2.writerow([sf_ecdf.x[i], sf_ecdf.y[i], "SourceForge"])

for i in range(len(gh_ecdf.x)):
    csvwriter2.writerow([gh_ecdf.x[i], gh_ecdf.y[i], "GitHub"])

for i in range(len(gl_ecdf.x)):
    csvwriter2.writerow([gl_ecdf.x[i], gl_ecdf.y[i], "GitLab"])

for i in range(len(bb_ecdf.x)):
    csvwriter2.writerow([bb_ecdf.x[i], bb_ecdf.y[i], "Bitbucket"])

csv_file.close()
csv_file2.close()