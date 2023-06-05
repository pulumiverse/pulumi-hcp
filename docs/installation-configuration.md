---
title: HashiCorp Cloud Platform (HCP) Installation & Configuration
meta_desc: Information on how to install theHashiCorp Cloud Platform (HCP) Provider for Pulumi.
layout: installation
---

## Installation

The Pulumi HashiCorp Cloud Platform (HCP) provider is available as a package in the following Pulumi languages:

* JavaScript/TypeScript: [`@pulumiverse/hcp`](https://www.npmjs.com/package/@grapl/pulumi-hcp)
* Python: [`pulumiverse_hcp`](https://pypi.org/project/pulumiverse-hcp/)
* Go: [`github.com/pulumiverse/pulumi-hcp/sdk`](https://pkg.go.dev/github.com/pulumiverse/pulumi-hcp/sdk)

## Setup

To provision resources with the Pulumi HCP provider, you need to have
HCP credentials.

### Set environment variables

Once you have provisioned these credentials, you can set environment
variables to provision resources in HCP:

{{< chooser os "linux,macos,windows" >}}
{{% choosable os linux %}}

```bash
$ export HCP_CLIENT_ID=<HCP_CLIENT_ID>
$ export HCP_CLIENT_SECRET=<HCP_CLIENT_SECRET>
```

{{% /choosable %}}

{{% choosable os macos %}}

```bash
$ export HCP_CLIENT_ID=<HCP_CLIENT_ID>
$ export HCP_CLIENT_SECRET=<HCP_CLIENT_SECRET>
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:HCP_CLIENT_ID = "<HCP_CLIENT_ID>"
> $env:HCP_CLIENT_SECRET = "<HCP_CLIENT_SECRET>"
```

{{% /choosable %}}
{{< /chooser >}}

## Configuration Options

Use `pulumi config set hcp:<option>` or pass options to the [constructor of `new hcp.Provider`]({{< relref "/registry/packages/hcp/api-docs/provider" >}}).

| Option          | Required/Optional | Description                                                                                                       |
|-----------------|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `client_id`     | Required          | The OAuth2 Client ID for API operations. Can be configured from the environment variable `HCP_CLIENT_ID`.         |
| `client_secret` | Required          | The OAuth2 Client Secret for API operations. Can be configured from the environment variable `HCP_CLIENT_SECRET`. |
