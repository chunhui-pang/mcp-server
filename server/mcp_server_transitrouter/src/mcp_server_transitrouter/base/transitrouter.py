import volcenginesdkcore

from mcp_server_transitrouter.base.config import TR_CONFIG
from volcenginesdktransitrouter.api.transitrouter_api import TRANSITROUTERApi

from volcenginesdktransitrouter.models import \
    CreateTransitRouterRequest, CreateTransitRouterResponse, \
    DescribeTransitRoutersRequest, DescribeTransitRoutersResponse, \
    DescribeTransitRouterAttachmentsRequest, DescribeTransitRouterAttachmentsResponse, \
    CreateTransitRouterVpcAttachmentRequest, CreateTransitRouterVpcAttachmentResponse, \
    DescribeTransitRouterVpcAttachmentsRequest, DescribeTransitRouterVpcAttachmentsResponse, \
    CreateTransitRouterVpnAttachmentRequest, CreateTransitRouterVpnAttachmentResponse, \
    DescribeTransitRouterVpnAttachmentsRequest, DescribeTransitRouterVpnAttachmentsResponse, \
    CreateTransitRouterDirectConnectGatewayAttachmentRequest, CreateTransitRouterDirectConnectGatewayAttachmentResponse, \
    DescribeTransitRouterDirectConnectGatewayAttachmentsRequest, DescribeTransitRouterDirectConnectGatewayAttachmentsResponse, \
    CreateTransitRouterPeerAttachmentRequest, CreateTransitRouterPeerAttachmentResponse, \
    DescribeTransitRouterPeerAttachmentsRequest, DescribeTransitRouterPeerAttachmentsResponse, \
    CreateTransitRouterRouteTableRequest, CreateTransitRouterRouteTableResponse, \
    DescribeTransitRouterRouteTablesRequest, DescribeTransitRouterRouteTablesResponse, \
    CreateTransitRouterRouteEntryRequest, CreateTransitRouterRouteEntryResponse, \
    DescribeTransitRouterRouteEntriesRequest, DescribeTransitRouterRouteEntriesResponse, \
    AssociateTransitRouterAttachmentToRouteTableRequest, AssociateTransitRouterAttachmentToRouteTableResponse, \
    DescribeTransitRouterRouteTableAssociationsRequest, DescribeTransitRouterRouteTableAssociationsResponse, \
    EnableTransitRouterRouteTablePropagationRequest, EnableTransitRouterRouteTablePropagationResponse, \
    DescribeTransitRouterRouteTablePropagationsRequest, DescribeTransitRouterRouteTablePropagationsResponse, \
    CreateTransitRouterRoutePolicyTableRequest, CreateTransitRouterRoutePolicyTableResponse, \
    AssociateTransitRouterRoutePolicyToRouteTableRequest, AssociateTransitRouterRoutePolicyToRouteTableResponse, \
    DescribeTransitRouterRoutePolicyTablesRequest, DescribeTransitRouterRoutePolicyTablesResponse, \
    CreateTransitRouterRoutePolicyEntryRequest, CreateTransitRouterRoutePolicyEntryResponse, \
    DescribeTransitRouterRoutePolicyEntriesRequest, DescribeTransitRouterRoutePolicyEntriesResponse, \
    CreateTransitRouterForwardPolicyTableRequest, CreateTransitRouterForwardPolicyTableResponse, \
    AssociateTransitRouterForwardPolicyTableToAttachmentRequest, AssociateTransitRouterForwardPolicyTableToAttachmentResponse, \
    DescribeTransitRouterForwardPolicyTablesRequest, DescribeTransitRouterForwardPolicyTablesResponse, \
    CreateTransitRouterForwardPolicyEntryRequest, CreateTransitRouterForwardPolicyEntryResponse, \
    DescribeTransitRouterForwardPolicyEntriesRequest, DescribeTransitRouterForwardPolicyEntriesResponse, \
    CreateTransitRouterFlowLogRequest, CreateTransitRouterFlowLogResponse, \
    StartTransitRouterFlowLogRequest, StartTransitRouterFlowLogResponse, \
    StopTransitRouterFlowLogRequest, StopTransitRouterFlowLogResponse, \
    DescribeTransitRouterFlowLogsRequest, DescribeTransitRouterFlowLogsResponse, \
    CreateTransitRouterTrafficQosMarkingPolicyRequest, CreateTransitRouterTrafficQosMarkingPolicyResponse, \
    AssociateTransitRouterTrafficQosMarkingPolicyToAttachmentRequest, AssociateTransitRouterTrafficQosMarkingPolicyToAttachmentResponse, \
    DescribeTransitRouterTrafficQosMarkingPoliciesRequest, DescribeTransitRouterTrafficQosMarkingPoliciesResponse, \
    CreateTransitRouterTrafficQosMarkingEntryRequest, CreateTransitRouterTrafficQosMarkingEntryResponse, \
    DescribeTransitRouterTrafficQosMarkingEntriesRequest, DescribeTransitRouterTrafficQosMarkingEntriesResponse, \
    CreateTransitRouterTrafficQosQueuePolicyRequest, CreateTransitRouterTrafficQosQueuePolicyResponse, \
    AssociateTransitRouterTrafficQosQueuePolicyToAttachmentRequest, AssociateTransitRouterTrafficQosQueuePolicyToAttachmentResponse, \
    DescribeTransitRouterTrafficQosQueuePoliciesRequest, DescribeTransitRouterTrafficQosQueuePoliciesResponse, \
    CreateTransitRouterTrafficQosQueueEntryRequest, CreateTransitRouterTrafficQosQueueEntryResponse, \
    DescribeTransitRouterTrafficQosQueueEntriesRequest, DescribeTransitRouterTrafficQosQueueEntriesResponse, \
    CreateTransitRouterMulticastDomainRequest, CreateTransitRouterMulticastDomainResponse, \
    DescribeTransitRouterMulticastDomainsRequest, DescribeTransitRouterMulticastDomainsResponse, \
    AssociateTransitRouterMulticastDomainRequest, AssociateTransitRouterMulticastDomainResponse, \
    DescribeTransitRouterMulticastDomainAssociationsRequest, DescribeTransitRouterMulticastDomainAssociationsResponse, \
    CreateTransitRouterMulticastGroupMemberRequest, CreateTransitRouterMulticastGroupMemberResponse, \
    CreateTransitRouterMulticastGroupSourceRequest, CreateTransitRouterMulticastGroupSourceResponse, \
    DescribeTransitRouterMulticastGroupsRequest, DescribeTransitRouterMulticastGroupsResponse, \
    DescribeTransitRouterRegionsRequest, DescribeTransitRouterRegionsResponse, \
    CreateTransitRouterBandwidthPackageRequest, CreateTransitRouterBandwidthPackageResponse, \
    RenewTransitRouterBandwidthPackageRequest, RenewTransitRouterBandwidthPackageResponse, \
    SetTransitRouterBandwidthPackageRenewalRequest, SetTransitRouterBandwidthPackageRenewalResponse, \
    DescribeTransitRouterBandwidthPackagesRequest, DescribeTransitRouterBandwidthPackagesResponse, \
    DescribeTransitRouterBandwidthPackagesBillingRequest, DescribeTransitRouterBandwidthPackagesBillingResponse


class TRSDK:
    """初始化 Volc TR SDK client"""

    def __init__(self):
        configuration = volcenginesdkcore.Configuration()
        configuration.ak = TR_CONFIG.access_key
        configuration.sk = TR_CONFIG.secret_key
        configuration.region = TR_CONFIG.region
        if TR_CONFIG.host is not None:
            configuration.host = TR_CONFIG.host
        self.client = TRANSITROUTERApi(volcenginesdkcore.ApiClient(configuration))

    def create_transit_router(self, args: dict) -> CreateTransitRouterResponse:
        return self.client.create_transit_router(CreateTransitRouterRequest(**args))

    def describe_transit_routers(self, args: dict) -> DescribeTransitRoutersResponse:
        return self.client.describe_transit_routers(DescribeTransitRoutersRequest(**args))

    def describe_transit_router_attachments(self, args: dict) -> DescribeTransitRouterAttachmentsResponse:
        return self.client.describe_transit_router_attachments(DescribeTransitRouterAttachmentsRequest(**args))

    def create_transit_router_vpc_attachment(self, args: dict) -> CreateTransitRouterVpcAttachmentResponse:
        return self.client.create_transit_router_vpc_attachment(CreateTransitRouterVpcAttachmentRequest(**args))

    def describe_transit_router_vpc_attachments(self, args: dict) -> DescribeTransitRouterVpcAttachmentsResponse:
        return self.client.describe_transit_router_vpc_attachments(DescribeTransitRouterVpcAttachmentsRequest(**args))

    def create_transit_router_vpn_attachment(self, args: dict) -> CreateTransitRouterVpnAttachmentResponse:
        return self.client.create_transit_router_vpn_attachment(CreateTransitRouterVpnAttachmentRequest(**args))

    def describe_transit_router_vpn_attachments(self, args: dict) -> DescribeTransitRouterVpnAttachmentsResponse:
        return self.client.describe_transit_router_vpn_attachments(DescribeTransitRouterVpnAttachmentsRequest(**args))

    def create_transit_router_direct_connect_gateway_attachment(self, args: dict) -> CreateTransitRouterDirectConnectGatewayAttachmentResponse:
        return self.client.create_transit_router_direct_connect_gateway_attachment(CreateTransitRouterDirectConnectGatewayAttachmentRequest(**args))

    def describe_transit_router_direct_connect_gateway_attachments(self, args: dict) -> DescribeTransitRouterDirectConnectGatewayAttachmentsResponse:
        return self.client.describe_transit_router_direct_connect_gateway_attachments(DescribeTransitRouterDirectConnectGatewayAttachmentsRequest(**args))

    def create_transit_router_peer_attachment(self, args: dict) -> CreateTransitRouterPeerAttachmentResponse:
        return self.client.create_transit_router_peer_attachment(CreateTransitRouterPeerAttachmentRequest(**args))

    def describe_transit_router_peer_attachments(self, args: dict) -> DescribeTransitRouterPeerAttachmentsResponse:
        return self.client.describe_transit_router_peer_attachments(DescribeTransitRouterPeerAttachmentsRequest(**args))

    def create_transit_router_route_table(self, args: dict) -> CreateTransitRouterRouteTableResponse:
        return self.client.create_transit_router_route_table(CreateTransitRouterRouteTableRequest(**args))

    def describe_transit_router_route_tables(self, args: dict) -> DescribeTransitRouterRouteTablesResponse:
        return self.client.describe_transit_router_route_tables(DescribeTransitRouterRouteTablesRequest(**args))

    def create_transit_router_route_entry(self, args: dict) -> CreateTransitRouterRouteEntryResponse:
        return self.client.create_transit_router_route_entry(CreateTransitRouterRouteEntryRequest(**args))

    def describe_transit_router_route_entries(self, args: dict) -> DescribeTransitRouterRouteEntriesResponse:
        return self.client.describe_transit_router_route_entries(DescribeTransitRouterRouteEntriesRequest(**args))

    def associate_transit_router_attachment_to_route_table(self, args: dict) -> AssociateTransitRouterAttachmentToRouteTableResponse:
        return self.client.associate_transit_router_attachment_to_route_table(AssociateTransitRouterAttachmentToRouteTableRequest(**args))

    def describe_transit_router_route_table_associations(self, args: dict) -> DescribeTransitRouterRouteTableAssociationsResponse:
        return self.client.describe_transit_router_route_table_associations(DescribeTransitRouterRouteTableAssociationsRequest(**args))

    def enable_transit_router_route_table_propagation(self, args: dict) -> EnableTransitRouterRouteTablePropagationResponse:
        return self.client.enable_transit_router_route_table_propagation(EnableTransitRouterRouteTablePropagationRequest(**args))

    def describe_transit_router_route_table_propagations(self, args: dict) -> DescribeTransitRouterRouteTablePropagationsResponse:
        return self.client.describe_transit_router_route_table_propagations(DescribeTransitRouterRouteTablePropagationsRequest(**args))

    def create_transit_router_route_policy_table(self, args: dict) -> CreateTransitRouterRoutePolicyTableResponse:
        return self.client.create_transit_router_route_policy_table(CreateTransitRouterRoutePolicyTableRequest(**args))

    def associate_transit_router_route_policy_to_route_table(self, args: dict) -> AssociateTransitRouterRoutePolicyToRouteTableResponse:
        return self.client.associate_transit_router_route_policy_to_route_table(AssociateTransitRouterRoutePolicyToRouteTableRequest(**args))

    def describe_transit_router_route_policy_tables(self, args: dict) -> DescribeTransitRouterRoutePolicyTablesResponse:
        return self.client.describe_transit_router_route_policy_tables(DescribeTransitRouterRoutePolicyTablesRequest(**args))

    def create_transit_router_route_policy_entry(self, args: dict) -> CreateTransitRouterRoutePolicyEntryResponse:
        return self.client.create_transit_router_route_policy_entry(CreateTransitRouterRoutePolicyEntryRequest(**args))

    def describe_transit_router_route_policy_entries(self, args: dict) -> DescribeTransitRouterRoutePolicyEntriesResponse:
        return self.client.describe_transit_router_route_policy_entries(DescribeTransitRouterRoutePolicyEntriesRequest(**args))

    def create_transit_router_forward_policy_table(self, args: dict) -> CreateTransitRouterForwardPolicyTableResponse:
        return self.client.create_transit_router_forward_policy_table(CreateTransitRouterForwardPolicyTableRequest(**args))

    def associate_transit_router_forward_policy_table_to_attachment(self, args: dict) -> AssociateTransitRouterForwardPolicyTableToAttachmentResponse:
        return self.client.associate_transit_router_forward_policy_table_to_attachment(AssociateTransitRouterForwardPolicyTableToAttachmentRequest(**args))

    def describe_transit_router_forward_policy_tables(self, args: dict) -> DescribeTransitRouterForwardPolicyTablesResponse:
        return self.client.describe_transit_router_forward_policy_tables(DescribeTransitRouterForwardPolicyTablesRequest(**args))

    def create_transit_router_forward_policy_entry(self, args: dict) -> CreateTransitRouterForwardPolicyEntryResponse:
        return self.client.create_transit_router_forward_policy_entry(CreateTransitRouterForwardPolicyEntryRequest(**args))

    def describe_transit_router_forward_policy_entries(self, args: dict) -> DescribeTransitRouterForwardPolicyEntriesResponse:
        return self.client.describe_transit_router_forward_policy_entries(DescribeTransitRouterForwardPolicyEntriesRequest(**args))

    def create_transit_router_flow_log(self, args: dict) -> CreateTransitRouterFlowLogResponse:
        return self.client.create_transit_router_flow_log(CreateTransitRouterFlowLogRequest(**args))

    def start_transit_router_flow_log(self, args: dict) -> StartTransitRouterFlowLogResponse:
        return self.client.start_transit_router_flow_log(StartTransitRouterFlowLogRequest(**args))

    def stop_transit_router_flow_log(self, args: dict) -> StopTransitRouterFlowLogResponse:
        return self.client.stop_transit_router_flow_log(StopTransitRouterFlowLogRequest(**args))

    def describe_transit_router_flow_logs(self, args: dict) -> DescribeTransitRouterFlowLogsResponse:
        return self.client.describe_transit_router_flow_logs(DescribeTransitRouterFlowLogsRequest(**args))

    def create_transit_router_traffic_qos_marking_policy(self, args: dict) -> CreateTransitRouterTrafficQosMarkingPolicyResponse:
        return self.client.create_transit_router_traffic_qos_marking_policy(CreateTransitRouterTrafficQosMarkingPolicyRequest(**args))

    def associate_transit_router_traffic_qos_marking_policy_to_attachment(self, args: dict) -> AssociateTransitRouterTrafficQosMarkingPolicyToAttachmentResponse:
        return self.client.associate_transit_router_traffic_qos_marking_policy_to_attachment(AssociateTransitRouterTrafficQosMarkingPolicyToAttachmentRequest(**args))

    def describe_transit_router_traffic_qos_marking_policies(self, args: dict) -> DescribeTransitRouterTrafficQosMarkingPoliciesResponse:
        return self.client.describe_transit_router_traffic_qos_marking_policies(DescribeTransitRouterTrafficQosMarkingPoliciesRequest(**args))

    def create_transit_router_traffic_qos_marking_entry(self, args: dict) -> CreateTransitRouterTrafficQosMarkingEntryResponse:
        return self.client.create_transit_router_traffic_qos_marking_entry(CreateTransitRouterTrafficQosMarkingEntryRequest(**args))

    def describe_transit_router_traffic_qos_marking_entries(self, args: dict) -> DescribeTransitRouterTrafficQosMarkingEntriesResponse:
        return self.client.describe_transit_router_traffic_qos_marking_entries(DescribeTransitRouterTrafficQosMarkingEntriesRequest(**args))

    def create_transit_router_traffic_qos_queue_policy(self, args: dict) -> CreateTransitRouterTrafficQosQueuePolicyResponse:
        return self.client.create_transit_router_traffic_qos_queue_policy(CreateTransitRouterTrafficQosQueuePolicyRequest(**args))

    def associate_transit_router_traffic_qos_queue_policy_to_attachment(self, args: dict) -> AssociateTransitRouterTrafficQosQueuePolicyToAttachmentResponse:
        return self.client.associate_transit_router_traffic_qos_queue_policy_to_attachment(AssociateTransitRouterTrafficQosQueuePolicyToAttachmentRequest(**args))

    def describe_transit_router_traffic_qos_queue_policies(self, args: dict) -> DescribeTransitRouterTrafficQosQueuePoliciesResponse:
        return self.client.describe_transit_router_traffic_qos_queue_policies(DescribeTransitRouterTrafficQosQueuePoliciesRequest(**args))

    def create_transit_router_traffic_qos_queue_entry(self, args: dict) -> CreateTransitRouterTrafficQosQueueEntryResponse:
        return self.client.create_transit_router_traffic_qos_queue_entry(CreateTransitRouterTrafficQosQueueEntryRequest(**args))

    def describe_transit_router_traffic_qos_queue_entries(self, args: dict) -> DescribeTransitRouterTrafficQosQueueEntriesResponse:
        return self.client.describe_transit_router_traffic_qos_queue_entries(DescribeTransitRouterTrafficQosQueueEntriesRequest(**args))

    def create_transit_router_multicast_domain(self, args: dict) -> CreateTransitRouterMulticastDomainResponse:
        return self.client.create_transit_router_multicast_domain(CreateTransitRouterMulticastDomainRequest(**args))

    def describe_transit_router_multicast_domains(self, args: dict) -> DescribeTransitRouterMulticastDomainsResponse:
        return self.client.describe_transit_router_multicast_domains(DescribeTransitRouterMulticastDomainsRequest(**args))

    def associate_transit_router_multicast_domain(self, args: dict) -> AssociateTransitRouterMulticastDomainResponse:
        return self.client.associate_transit_router_multicast_domain(AssociateTransitRouterMulticastDomainRequest(**args))

    def describe_transit_router_multicast_domain_associations(self, args: dict) -> DescribeTransitRouterMulticastDomainAssociationsResponse:
        return self.client.describe_transit_router_multicast_domain_associations(DescribeTransitRouterMulticastDomainAssociationsRequest(**args))

    def create_transit_router_multicast_group_member(self, args: dict) -> CreateTransitRouterMulticastGroupMemberResponse:
        return self.client.create_transit_router_multicast_group_member(CreateTransitRouterMulticastGroupMemberRequest(**args))

    def create_transit_router_multicast_group_source(self, args: dict) -> CreateTransitRouterMulticastGroupSourceResponse:
        return self.client.create_transit_router_multicast_group_source(CreateTransitRouterMulticastGroupSourceRequest(**args))

    def describe_transit_router_multicast_groups(self, args: dict) -> DescribeTransitRouterMulticastGroupsResponse:
        return self.client.describe_transit_router_multicast_groups(DescribeTransitRouterMulticastGroupsRequest(**args))

    def describe_transit_router_regions(self, args: dict) -> DescribeTransitRouterRegionsResponse:
        return self.client.describe_transit_router_regions(DescribeTransitRouterRegionsRequest(**args))

    def create_transit_router_bandwidth_package(self, args: dict) -> CreateTransitRouterBandwidthPackageResponse:
        return self.client.create_transit_router_bandwidth_package(CreateTransitRouterBandwidthPackageRequest(**args))

    def renew_transit_router_bandwidth_package(self, args: dict) -> RenewTransitRouterBandwidthPackageResponse:
        return self.client.renew_transit_router_bandwidth_package(RenewTransitRouterBandwidthPackageRequest(**args))

    def set_transit_router_bandwidth_package_renewal(self, args: dict) -> SetTransitRouterBandwidthPackageRenewalResponse:
        return self.client.set_transit_router_bandwidth_package_renewal(SetTransitRouterBandwidthPackageRenewalRequest(**args))

    def describe_transit_router_bandwidth_packages(self, args: dict) -> DescribeTransitRouterBandwidthPackagesResponse:
        return self.client.describe_transit_router_bandwidth_packages(DescribeTransitRouterBandwidthPackagesRequest(**args))

    def describe_transit_router_bandwidth_packages_billing(self, args: dict) -> DescribeTransitRouterBandwidthPackagesBillingResponse:
        return self.client.describe_transit_router_bandwidth_packages_billing(DescribeTransitRouterBandwidthPackagesBillingRequest(**args))
