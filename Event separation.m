% clear all
%%DATI INPUT
hdry=2;
giorni=24;

%%%%%%%%%%%%%%%%%%%%%%%     SELEZIONE EVENTI    %%%%%%%%%%%%%%%%%%%%%%%%%%%
%FIND DRY PERIOD
%h max
h=hdry;
%giorni
step=giorni;
index=[];
tot=0;
k=25;

while k<length(rain)

    end_index=0;
    
    j=0;
    
    if sum(rain(k-step+1:k))>=h && sum(rain(k:k+step-1))>= h  
        
        start_index=k;
        
        for j=start_index:length(rain)-1
            
            if sum(rain(k:j)) >= h && sum(rain(j+1:j+step))< h
                
                end_index=j;
                
                 tot=tot+1;
                
                index(tot,1)=start_index;
                
                index(tot,2)=end_index;
                
                k=j+step+1; 
                
                break
            
            end
                       
        end
        
    end
    
    if end_index==0
        
        k=k+1;
        
    end
    
    disp(k);
    
end

index2=index';

%DURATE TUTTI GLI EVENTI [h]
for k=1:length(index) 
     DURATE(k,1)=((index2(2,k)-index2(1,k))+1);  
end

%H cumulated TUTTI GLI EVENTI [mm]
for k=1:length(index) 
     H(k,1)=sum(rain(index2(1,k):index2(2,k)));
end 

%Intensità MEDIA TUTTI GLI EVENTI [mm/g]
for k=1:length(index) 
     Imedia(k,1)=(H(k,1))/(DURATE(k,1));
end