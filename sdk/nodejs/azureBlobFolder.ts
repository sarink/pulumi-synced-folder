// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class AzureBlobFolder extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'synced-folder:index:AzureBlobFolder';

    /**
     * Returns true if the given object is an instance of AzureBlobFolder.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AzureBlobFolder {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AzureBlobFolder.__pulumiType;
    }


    /**
     * Create a AzureBlobFolder resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AzureBlobFolderArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.containerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'containerName'");
            }
            if ((!args || args.path === undefined) && !opts.urn) {
                throw new Error("Missing required property 'path'");
            }
            if ((!args || args.resourceGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.storageAccountName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageAccountName'");
            }
            resourceInputs["containerName"] = args ? args.containerName : undefined;
            resourceInputs["managedObjects"] = args ? args.managedObjects : undefined;
            resourceInputs["path"] = args ? args.path : undefined;
            resourceInputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            resourceInputs["storageAccountName"] = args ? args.storageAccountName : undefined;
        } else {
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AzureBlobFolder.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a AzureBlobFolder resource.
 */
export interface AzureBlobFolderArgs {
    /**
     * The name of the Azure storage container to sync to. Required.
     */
    containerName: pulumi.Input<string>;
    /**
     * Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
     */
    managedObjects?: pulumi.Input<boolean>;
    /**
     * The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
     */
    path: pulumi.Input<string>;
    /**
     * The name of the Azure resource group that the storage account belongs to. Required.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * The name of the Azure storage account that the container belongs to. Required.
     */
    storageAccountName: pulumi.Input<string>;
}
