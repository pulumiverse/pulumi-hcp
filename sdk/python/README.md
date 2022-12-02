# HCP Resource Provider

The HCP Resource Provider lets you manage [Hashicorp Cloud Platform](https://cloud.hashicorp.com/) resources.

**NOTE**: This provider is in the process of being migrated to the
[Pulumiverse](https://github.com/pulumiverse) organization. Make note
of the upcoming package name changes below for your SDK.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @grapl/pulumi-hcp
```
Or, following the Pulumiverse migration:
```bash
npm install @pulumiverse/hcp
```

or `yarn`:

```bash
yarn add @grapl/pulumi-hcp
```
Or, following the Pulumiverse migration:
```bash
yarn add @pulumiverse/hcp
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_hcp
```
Or, following the Pulumiverse migration:
```bash
pip install pulumiverse_hcp
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/grapl-security/pulumi-hcp/sdk/go/...
```
Or, following the Pulumiverse migration:
```bash
go get github.com/pulumiverse/pulumi-hcp/sdk/go/...
```

## Configuration

The following configuration points are available for the `hcp` provider:

- `hcp:clientId` (environment: `HCP_CLIENT_ID`) - The OAuth2 Client ID for API operations.
- `hcp:clientSecret` (environment: `HCP_CLIENT_SECRET`) - The OAuth2 Client Secret for API operations.

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/hcp/api-docs/).
