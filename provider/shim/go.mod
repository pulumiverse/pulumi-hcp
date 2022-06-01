module github.com/hashicorp/terraform-provider-hcp/shim

go 1.16

require (
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.17.0
	github.com/hashicorp/terraform-provider-hcp v0.30.0
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220523144019-a9dc436975cc
