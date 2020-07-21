"""
Created on Sun Jun 28 17:15:52 2020
"""
#metodo para buscar un subarray que su suma valga S
# ini es el inicio del subarray
# end es el final del subarray
# A es la longitud del array original
# N es el array original
# S es el valor suma deseado
 
def serchsub(ini,end,A,N,S):
    if(end<A):
        v=sum(N[ini:(end+1)])        
        if v < S:
            end=end+1
            return serchsub(ini,end,A,N,S)
        if v == S:
            #print('entre al caso V = S')
            return 'el sub string inicia en N[{}] y termina incluyendo N[{}]'.format(ini,end)           
        if v > S:
            ini=ini+1
            return serchsub(ini,end,A,N,S)
    else:
        return('no esta')
    
S=11
N=[1,2,3,4,5,9,11]
A=len(N)
ini=0
end=0
suma=0
u=serchsub(ini,end,A,N,S)
print(u)

 

    
    
    
    
        
    

    

        
         
    