module github.com/hashicorp/terraform-provider-hcp/shim

go 1.16

require (
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.19.0
	github.com/hashicorp/terraform-provider-hcp v0.37.0
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220725190814-23001ad6ec03
