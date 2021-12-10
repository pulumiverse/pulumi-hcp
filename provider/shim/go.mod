module github.com/hashicorp/terraform-provider-hcp/shim

go 1.15

require (
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.10.0
	github.com/hashicorp/terraform-provider-hcp v0.21.1
//-20211209205119-ff2116cec1d6
)

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20201218231525-9cca98608a5e
