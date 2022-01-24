// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

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

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(shim.NewProvider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "hcp",
		Description: "A Pulumi package for creating and managing hcp cloud resources.",
		Keywords:    []string{"pulumi", "hcp"},
		License:     "Apache-2.0",
		Homepage:    "https://pulumi.io",
		GitHubOrg:   "hashicorp",
		Repository:  "https://github.com/grapl-security/pulumi-hcp",
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
			},
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"hcp_aws_network_peering":            {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AwsNetworkPeering")},
			"hcp_aws_transit_gateway_attachment": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "AwsTransitGatewayAttachment")},
			"hcp_consul_cluster":                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConsulCluster")},
			"hcp_consul_cluster_root_token":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConsulClusterRootToken")},
			"hcp_consul_snapshot":                {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ConsulSnapshot")},
			"hcp_hvn":                            {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Hvn")},
			"hcp_hvn_peering_connection":         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "HvnPeeringConnection")},
			"hcp_hvn_route":                      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "HvnRoute")},
			"hcp_vault_cluster":                  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "VaultCluster")},
			"hcp_vault_cluster_admin_token":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "VaultClusterAdminToken")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"hcp_aws_network_peering": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAwsNetworkPeering")},
			"hcp_aws_transit_gateway_attachment": {Tok: tfbridge.MakeDataSource(
				mainPkg, mainMod, "getAwsTransitGatewayAttachment",
			)},
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
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
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
