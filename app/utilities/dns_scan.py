from cmath import e
from mimetypes import init
import dns
import json
import dns.resolver

#schemes
from schemes.dns import DnsBase, ResponseDns

class Read_DNS:

    def read_DNS(db_domain, result_create_DNS):

        print("result-create-DNS")

        print(result_create_DNS)
        try:
            dict_temp={}
            ansMX = dns.resolver.resolve(db_domain.nombre_dominio, 'MX')
            ansA = dns.resolver.resolve(db_domain.nombre_dominio, 'A')
            ansAAAA = dns.resolver.resolve(db_domain.nombre_dominio, 'AAAA')
            ansNS = dns.resolver.resolve(db_domain.nombre_dominio, 'NS')
            ansSOA = dns.resolver.resolve(db_domain.nombre_dominio, 'SOA')
            ansTXT = dns.resolver.resolve(db_domain.nombre_dominio, 'TXT')

            for anMX, anA, anAAAA, anNS, anSOA, anTXT  in zip(ansMX,ansA, ansAAAA,
                                                            ansNS, ansSOA, ansTXT    ):
                
                dict_temp = {
                    'MX': 1 ,'data':anMX,'A': 2, 'data': anA,
                    'AAAA': 3, 'data': anAAAA,'NS': 4, 'data': anNS,
                    'SOA': 5, 'data': anSOA,'TXT': 6, 'data': anTXT
                }

            ##model_response: DnsBase = {dict_temp['MX'],69,dict_temp['data']}

            model_response = DnsBase(id_tipo=2,id_dominio=db_domain.id_dominio,nombre_dns='example2.com')

            print(model_response)

            return (model_response)
        
        except Exception as e:
            print(e)

        
        



