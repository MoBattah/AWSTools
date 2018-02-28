for regions in `aws ec2 describe-regions --output text|awk {'print $3'}`
do
   for volumes in `aws ec2 describe-volumes --region $regions --output text| grep available | awk '{print $9}' | grep vol| tr '\n' ' '`
    do
 echo $regions" "$volumes
 done
done
