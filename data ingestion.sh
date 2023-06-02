URL=http://cacib.opensee.ninja:9999
account=user_name
passwd=****
tableName=LiquidityGAP14
ziptableName=GapTimeBucket14
comment=Ingestion
branch=branch_name
token=$(curl --insecure -X POST -d '{"identifier": "'${account}'","password": "'${passwd}'"}' ${URL}/login | awk '{match($0, /\{"token":"([^"]*).*"/, arr); print arr[1];}');
echo $token
curl --insecure -X POST -H "Authorization: ${token}" -H "Content-Type: application/json" --data-binary @LiquidityGAP14.json "${URL}/init_module";
for i in {11..15};  
do  
transactionId=$(curl --insecure -X POST -H "Authorization: ${token}" "${URL}/tables/${tableName}/transaction/2023-05-${i}/from/${branch}/${comment}"); 
echo $transactionId;
for j in {0..2}; 
do 
curl --insecure -X POST -H "Authorization: ${token}" -H "Content-Type: text/csv" --data-binary @13GapTimeBucket10_${j}.csv "${URL}/tables/${ziptableName}/2023-05-${i}";
done;
curl --insecure -X POST -H "Authorization: ${token}" -H "Content-Type: text/csv" --data-binary @13LiquidityGAP10_${j}.csv "${URL}/tables/${tableName}/commits/${transactionId}/2023-05-${i}";
done; 
curl --insecure -X POST -H "Authorization: ${token}" "${URL}/tables/${tableName}/closeTransaction/${transactionId}/2023-05-${i}/to/${branch}"; 
done;




