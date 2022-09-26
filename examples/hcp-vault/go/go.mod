module vault-go

go 1.16

require (
	github.com/grapl-security/pulumi-hcp/sdk v0.1.11
	github.com/pulumi/pulumi/sdk/v3 v3.40.1
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220725190814-23001ad6ec03
