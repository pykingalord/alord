import dns.resolver
import os
os.system("color 1a")
os.system('cls')
url = input('Enter your link website >')
def DNScheck(url):
	DNS_list_types = ['A','AAAA','MX','CNAME','NS','SRV','AFSDB','APL','CAA','CDNSKEY','CDS','CERT','DHCID','DLV','DNSKEY','DS','HIP','IPSECKEY','KEY','KX','LOC','NAPTR','NSEC','NSEC3','NSEC3PARAM','PTR','RRSIG','RP','CDS','SIG','SOA','SSHFP','TA','TLSA','TSIG','TXT','URI']
 	for dnstype in DNS_list_types:
 		DATE = dns.resolver.query(url,dnstype,raise_on_no_answer=False)
 		if DATE.rrset is not None:
 			print(DATE.rrset)
DNScheck(url)