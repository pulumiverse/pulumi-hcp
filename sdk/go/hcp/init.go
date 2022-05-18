// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "hcp:index/awsNetworkPeering:AwsNetworkPeering":
		r = &AwsNetworkPeering{}
	case "hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment":
		r = &AwsTransitGatewayAttachment{}
	case "hcp:index/azurePeeringConnection:AzurePeeringConnection":
		r = &AzurePeeringConnection{}
	case "hcp:index/consulCluster:ConsulCluster":
		r = &ConsulCluster{}
	case "hcp:index/consulClusterRootToken:ConsulClusterRootToken":
		r = &ConsulClusterRootToken{}
	case "hcp:index/consulSnapshot:ConsulSnapshot":
		r = &ConsulSnapshot{}
	case "hcp:index/hvn:Hvn":
		r = &Hvn{}
	case "hcp:index/hvnPeeringConnection:HvnPeeringConnection":
		r = &HvnPeeringConnection{}
	case "hcp:index/hvnRoute:HvnRoute":
		r = &HvnRoute{}
	case "hcp:index/vaultCluster:VaultCluster":
		r = &VaultCluster{}
	case "hcp:index/vaultClusterAdminToken:VaultClusterAdminToken":
		r = &VaultClusterAdminToken{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:hcp" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, _ := PkgVersion()
	pulumi.RegisterResourceModule(
		"hcp",
		"index/awsNetworkPeering",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/awsTransitGatewayAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/azurePeeringConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/consulCluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/consulClusterRootToken",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/consulSnapshot",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/hvn",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/hvnPeeringConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/hvnRoute",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/vaultCluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"hcp",
		"index/vaultClusterAdminToken",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"hcp",
		&pkg{version},
	)
}
