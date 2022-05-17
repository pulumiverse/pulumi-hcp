module github.com/grapl-security/pulumi-hcp/provider

go 1.16

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	// v0.16.0 removed the experimental tfinstall command
	// https://github.com/hashicorp/terraform-exec/blob/main/CHANGELOG.md#0160-january-31-2022
	github.com/hashicorp/terraform-exec => github.com/hashicorp/terraform-exec v0.15.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20211230170131-3a7c83bfab87
	github.com/hashicorp/terraform-provider-hcp/shim => ./shim
)

require (
	github.com/hashicorp/terraform-plugin-sdk v1.17.2 // indirect
	github.com/hashicorp/terraform-provider-hcp/shim v0.0.0-00010101000000-000000000000
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.20.0
	github.com/pulumi/pulumi/sdk/v3 v3.29.1
)
