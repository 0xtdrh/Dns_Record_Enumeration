import dns.resolver
import sys 
import os

record_types = ['A','AAAA','CNAME','MX','NS','TXT','PTR','SRV','CERT','DNAME']
# record_types = ['A','AAAA','CNAME','MX','NS']
try :
    domain = sys.argv[1]
except IndexError:
    print("syntax error => python3 ./dnsrecord.py {websitename}")
    quit()
for records in record_types :
    try :
        print("\n=========" + records + "=========\n")
        answer = dns.resolver.resolve(domain,records)
        for server in answer :
            print(server.to_text() + "\n")
    except dns.resolver.NoAnswer:
        print("None " + records)
    except dns.resolver.NXDOMAIN:
        os.system("clear")
        print(f"\n ============ {domain} does not exist. ============ \n")
        quit()
    except KeyboardInterrupt:
        print("\n ============ Good Bye! ============ \n")
        quit()
    except :
        pass