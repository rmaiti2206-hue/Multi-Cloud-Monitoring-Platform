# AWS live setup
Use a least-privilege IAM role. For cross-account monitoring, configure the backend runtime identity with sts:AssumeRole and enter the role ARN in Cloud Accounts. Same-account development can use the AWS SDK default credential chain. Never put AWS secrets in React.
