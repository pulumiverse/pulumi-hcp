package hcp

import (
	"fmt"
	"path/filepath"

	// This is code from *this* repository; the upstream provider places
	// its code in an `internal` directory, so we have to jump through
	// some hoops to access it.
	"github.com/hashicorp/terraform-provider-hcp/shim"

	"github.com/grapl-security/pulumi-hcp/provider/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tfshim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "hcp"
	// modules:
	mainMod = "index" // the hcp module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c tfshim.ResourceConfig) error {
	return nil
}

// boolRef returns a reference to the bool argument.
func boolRef(b bool) *bool {
	return &b
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(shim.NewProvider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "hcp",
		Description: "A Pulumi package for creating and managing HCP cloud resources.",
		// Keywords describing the provider in the Pulumi Registry.
		Keywords: []string{"pulumi", "hcp", "category/infrastructure"},
		License:  "Apache-2.0",
		Homepage: "https://pulumi.io",
		// The organization of the underlying Terraform provider we're
		// using, because it is not part of the `terraform-providers`
		// organization (this is required for proper documentation
		// extraction).
		GitHubOrg: "hashicorp",
		// The logo for this provider that will be shown in the Pulumi
		// Registry.
		LogoURL: "https://raw.githubusercontent.com/grapl-security/pulumi-hcp/main/assets/hcp.svg",
		// The repository for *this* code.
		Repository:  "https://github.com/grapl-security/pulumi-hcp",
		Publisher:   "Grapl Security",
		DisplayName: "HashiCorp Cloud Platform (HCP)",
		// Binaries for the plugin will be stored as Github Releases
		// (recommended by Pulumi).
		// NOTE: the added 'v' in front of `${VERSION}` is a temporary
		// workaround for (what I think is) a `pulumi plugin install` issue.
		PluginDownloadURL: "https://github.com/grapl-security/pulumi-hcp/releases/download/v${VERSION}",
		Config: map[string]*tfbridge.SchemaInfo{
			"client_id": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"HCP_CLIENT_ID"},
				},
			},
			"client_secret": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"HCP_CLIENT_SECRET"},
				},
				Secret: boolRef(true),
			},
		},
		PreConfigureCallback: preConfigureCallback,
		// Each resource from the underlying Terraform provider should
		// be reflected here.
		Resources: map[string]*tfbridge.ResourceInfo{
			"hcp_aws_network_peering":            {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AwsNetworkPeering")},
			"hcp_aws_transit_gateway_attachment": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AwsTransitGatewayAttachment")},
			"hcp_azure_peering_connection":       {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AzurePeeringConnection")},
			"hcp_consul_cluster":                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConsulCluster")},
			"hcp_consul_cluster_root_token":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConsulClusterRootToken")},
			"hcp_consul_snapshot":                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConsulSnapshot")},
			"hcp_hvn":                            {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Hvn")},
			"hcp_hvn_peering_connection":         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "HvnPeeringConnection")},
			"hcp_hvn_route":                      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "HvnRoute")},
			"hcp_vault_cluster":                  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "VaultCluster")},
			"hcp_vault_cluster_admin_token":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "VaultClusterAdminToken")},
		},
		// Each data source from the underlying Terraform provider
		// should be reflected here.
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"hcp_aws_network_peering": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAwsNetworkPeering")},
			"hcp_aws_transit_gateway_attachment": {Tok: tfbridge.MakeDataSource(
				mainPkg, mainMod, "getAwsTransitGatewayAttachment",
			)},
			"hcp_azure_peering_connection": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAzurePeeringConnection")},
			"hcp_consul_agent_helm_config": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getConsulAgentHelmConfig")},
			"hcp_consul_agent_kubernetes_secret": {Tok: tfbridge.MakeDataSource(
				mainPkg, mainMod, "getConsulAgentKubernetesSecret",
			)},
			"hcp_consul_cluster":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getConsulCluster")},
			"hcp_consul_versions":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getConsulVersions")},
			"hcp_hvn":                    {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getHvn")},
			"hcp_hvn_peering_connection": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getHvnPeeringConnection")},
			"hcp_hvn_route":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getHvnRoute")},
			"hcp_packer_image":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getPackerImage")},
			"hcp_packer_image_iteration": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getPackerImageIteration")},
			"hcp_packer_iteration":       {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getPackerIteration")},
			"hcp_vault_cluster":          {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getVaultCluster")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			PackageName: "@grapl/pulumi-hcp",
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/grapl-security/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
