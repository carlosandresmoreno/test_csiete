from cmath import e
import dns
import json
import dns.resolver

#schemes
from schemes.dns import DnsBase, ResponseDns

class Read_DNS:

    def read_DNS(db_domain, model_type_DNS):
        try:
            try:
                ans = dns.resolver.resolve(db_domain.nombre_dominio, model_type_DNS.nombre)              
                name = str(ans[0])
            except: 
                name = ""
            model_response = DnsBase(id_tipo=model_type_DNS.id_tipo,id_dominio=db_domain.id_dominio,nombre_dns=name)
            return (model_response)
        
        except Exception as e:
            print(e)

        
        



