def subdomainVisits(cpdomains: list[str]) -> list[str]:
    count_paired_domains = []

    # split number and strings
    for i in range(len(cpdomains)):
        cpdomains[i] = cpdomains[i].split(" ")

    # split strings to sub domain
    for i in range(len(cpdomains)):
        cpdomains[i][0] = int(cpdomains[i][0])
        cpdomains[i][1] = cpdomains[i][1].split(".")
    print(cpdomains)

    

    return count_paired_domains

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(f"Output: {subdomainVisits(cpdomains)}")