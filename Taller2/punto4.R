n<-5
c<-matrix(0,n,n+1)
for (i in 0:n){
  for (j in 0:(n+1)){
    c[i,j]=floor(runif(1, min=0, max=101))
  }
  
}

contador<-function(matriz){
  tot<-0
  for (i in 1:nrow(matriz)){
    p<-matriz[i,i]
    for (j in 1:ncol(matriz)){
      matriz[i,j]<-matriz[i,j]/p
      tot<-tot+1
    }
    for (j in 1:nrow(matriz)){
      if(j!=i){
        p<-matriz[j,i]
        for (k in 1:ncol(matriz)){
          matriz[j,k]<-matriz[j,k]-p*matriz[i,k]
          tot<-tot+1
        }
        
      }
    }
  }
  print(matriz)
  print("Número de operaciones: ")
  print(tot)
}

print(c)
contador(c)

