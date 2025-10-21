import logging
import os

from typing import Any, List, Optional, Dict
from mcp.server.fastmcp import FastMCP
from mcp_server_transitrouter.base.transitrouter import TRSDK

logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("TR MCP Server", port=int(os.getenv("PORT", "8008")))

tr_resource = TRSDK()


@mcp.tool(
    name="create_transit_router",
    description="创建一个中转路由器实例"
)
def create_transit_router(
        transit_router_name: Optional[str] = None,
        description: Optional[str] = None,
        project_name: Optional[str] = None,
        multicast_enabled: Optional[bool] = False,
        asn: Optional[int] = None,
        tags: Optional[List[Dict[str, str]]] = None,
        client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用CreateTransitRouter接口，创建一个中转路由器实例。
    Args:
        transit_router_name (str, optional): 中转路由器实例的名称。
        description (str, optional): 中转路由器实例的描述。
        project_name (str, optional): 中转路由器实例所属项目的名称。
        multicast_enabled (bool, optional): 是否启用组播功能。默认值为False。
        asn (int, optional): 自治系统号(ASN)，用于标识中转路由器的自治系统。
        tags (List[Dict[str, str]], optional): 标签列表，每个标签包含Key和Value。
        client_token (str, optional): 客户端Token，用于保证请求幂等性。
    Returns:
        dict[str, Any]: 创建的中转路由器实例信息。
    """
    req = {
        "transit_router_name": transit_router_name,
        "description": description,
        "project_name": project_name,
        "asn": asn,
        'tags': tags,
        "client_token": client_token,
    }
    if multicast_enabled is not None:
        req["multicast_enabled"] = multicast_enabled

    resp = tr_resource.create_transit_router(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_routers",
    description="查询满足指定条件的中转路由器实例"
)
def describe_transit_routers(
        transit_router_ids: Optional[List[str]] = None,
        transit_router_name: Optional[str] = None,
        project_name: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 DescribeTransitRouters 接口，查询满足指定条件的中转路由器实例。
    Args:
        transit_router_ids (List[str], optional): 中转路由器实例的ID列表。
        transit_router_name (str, optional): 中转路由器实例的名称。
        project_name (str, optional): 中转路由器实例所属项目的名称列表。
    Returns:
        dict[str, Any]: 中转路由器实例的详细信息。
    """
    req = {
        "transit_router_ids": transit_router_ids,
        "transit_router_name": transit_router_name,
        "project_name": project_name
    }

    resp = tr_resource.describe_transit_routers(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_attachments",
    description="查询满足指定条件的中转路由器实例"
)
def describe_transit_router_attachments(
        transit_router_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        transit_router_forward_policy_table_id: Optional[str] = None,
        transit_router_traffic_qos_marking_policy_id: Optional[str] = None,
        transit_router_traffic_qos_queue_policy_id: Optional[str] = None,
        transit_router_attachment_ids: Optional[List[str]] = None,
) -> dict[str, Any]:
    """
    调用 DescribeTransitRouterAttachments 接口，查询实例共享列表。
    Args:
        transit_router_id (str, optional): 中转路由器实例的ID。
        resource_type (str, optional): 资源类型。
        resource_id (str, optional): 资源ID。
        transit_router_forward_policy_table_id (str, optional): 路由策略表ID。
        transit_router_traffic_qos_marking_policy_id (str, optional): 流量QoS标记策略ID。
        transit_router_traffic_qos_queue_policy_id (str, optional): 流量QoS队列策略ID。
        transit_router_attachment_ids (List[str], optional): 网络实例连接的IDID列表。
    Returns:
        dict[str, Any]: 网络实例连接的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "resource_type": resource_type,
        "resource_id": resource_id,
        "transit_router_forward_policy_table_id": transit_router_forward_policy_table_id,
        "transit_router_traffic_qos_marking_policy_id": transit_router_traffic_qos_marking_policy_id,
        "transit_router_traffic_qos_queue_policy_id": transit_router_traffic_qos_queue_policy_id,
        "transit_router_attachment_ids": transit_router_attachment_ids,
    }

    resp = tr_resource.describe_transit_router_attachments(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_vpc_attachment",
    description="创建一个VPC类型的网络实例连接"
)
def create_transit_router_vpc_attachment(
        transit_router_id: str = None,
        vpc_id: str = None,
        attach_points: list = None,
        transit_router_attachment_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_publish_route_enabled: Optional[bool] = None,
        ipv6_enabled: Optional[bool] = None,
        appliance_mode_enabled: Optional[bool] = None,
        tags: Optional[list] = None,
        client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用CreateTransitRouterVpcAttachment接口，创建一个VPC类型的网络实例连接。
    Args:
        transit_router_id (str): 中转路由器实例ID。
        vpc_id (str): VPC实例ID。
        attach_points (list): 连接点配置列表，每个连接点需包含SubnetId和ZoneId。
        transit_router_attachment_name (str, optional): 网络实例连接的名称
        description (str, optional): 网络实例连接的描述信息
        auto_publish_route_enabled (bool, optional): 是否自动同步TR路由到网络实例路由表中
        ipv6_enabled (bool, optional): 是否开启IPv6功能
        appliance_mode_enabled (bool, optional): 是否开启路径一致模式
        tags (list, optional): 标签信息列表
        client_token (str, optional): 客户端Token，用于保证请求的幂等性
    Returns:
        dict[str, Any]: 创建的VPC类型网络实例连接信息
    """
    req = {
        "transit_router_id": transit_router_id,
        "vpc_id": vpc_id,
        "attach_points": attach_points,
        "transit_router_attachment_name": transit_router_attachment_name,
        "description": description,
        "tags": tags,
        "client_token": client_token,
    }
    if auto_publish_route_enabled is not None:
        req["auto_publish_route_enabled"] = auto_publish_route_enabled
    if ipv6_enabled is not None:
        req["ipv6_enabled"] = ipv6_enabled
    if appliance_mode_enabled is not None:
        req["appliance_mode_enabled"] = appliance_mode_enabled

    resp = tr_resource.create_transit_router_vpc_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_vpc_attachments",
    description="查询满足指定条件的VPC类型网络实例连接"
)
def describe_transit_router_vpc_attachments(
        transit_router_id: str = None,
        vpc_id: Optional[str] = None,
        transit_router_attachment_ids: Optional[List[str]] = None
) -> dict[str, Any]:
    """
    调用 DescribeTransitRouterVpcAttachments 接口，查询满足指定条件的VPC类型网络实例连接。
    Args:
        transit_router_id (str, optional): 中转路由器实例的ID。
        vpc_id (str, optional): VPC实例的ID。
        transit_router_attachment_ids (list[str], optional): 实例连接的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "vpc_id": vpc_id,
        "transit_router_attachment_ids": transit_router_attachment_ids
    }

    resp = tr_resource.describe_transit_router_vpc_attachments(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_vpn_attachment",
    description="创建一个VPN类型的网络实例连接"
)
def create_transit_router_vpn_attachment(
        transit_router_id: str = None,
        vpn_connection_id: str = None,
        transit_router_attachment_name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[Dict[str, str]]] = None,
        client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用CreateTransitRouterVpnAttachment接口，创建一个VPN类型的网络实例连接。
    Args:
        transit_router_id (str): 中转路由器实例ID。
        vpn_connection_id (str): VPN连接ID。
        transit_router_attachment_name (str, optional): 网络实例连接的名称。
        description (str, optional): 网络实例连接的描述信息。
        tags (List[Dict[str, str]], optional): 标签信息列表。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的VPN类型网络实例连接信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "vpn_connection_id": vpn_connection_id,
        "transit_router_attachment_name": transit_router_attachment_name,
        "description": description,
        "tags": tags,
        "client_token": client_token,
    }

    resp = tr_resource.create_transit_router_vpn_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_vpn_attachments",
    description="查询满足指定条件的VPN类型网络实例连接"
)
def describe_transit_router_vpn_attachments(
        transit_router_id: str = None,
        transit_router_attachment_ids: Optional[List[str]] = None,
        vpn_connection_id: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 describe_transit_router_vpn_attachments 接口，查询满足指定条件的VPN类型网络实例连接。
    Args:
        transit_router_id (str, optional): 中转路由器实例的ID。
        transit_router_attachment_ids (list[str], optional): VPN类型网络实例连接的ID列表。
        vpn_connection_id (str, optional): VPN连接的ID。
    Returns:
        dict[str, Any]: VPN类型网络实例连接的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_attachment_ids": transit_router_attachment_ids,
        "vpn_connection_id": vpn_connection_id,
    }

    resp = tr_resource.describe_transit_router_vpn_attachments(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_direct_connect_gateway_attachment",
    description="创建一个专线网关类型的网络实例连接"
)
def create_transit_router_direct_connect_gateway_attachment(
        transit_router_id: str = None,
        direct_connect_gateway_id: str = None,
        transit_router_attachment_name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[Dict[str, str]]] = None,
        client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用CreateTransitRouterDirectConnectGatewayAttachment接口，创建一个专线网关类型的网络实例连接。
    Args:
        transit_router_id (str): 中转路由器实例ID。
        direct_connect_gateway_id (str): 专线网关ID。
        transit_router_attachment_name (str, optional): 网络实例连接的名称。
        description (str, optional): 网络实例连接的描述信息。
        tags (List[Dict[str, str]], optional): 标签信息列表。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的专线网关类型网络实例连接信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "direct_connect_gateway_id": direct_connect_gateway_id,
        "transit_router_attachment_name": transit_router_attachment_name,
        "description": description,
        "tags": tags,
        "client_token": client_token,
    }

    resp = tr_resource.create_transit_router_direct_connect_gateway_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_direct_connect_gateway_attachments",
    description="查询满足指定条件的专线网关类型网络实例连接"
)
def describe_transit_router_direct_connect_gateway_attachments(
        transit_router_id: str = None,
        direct_connect_gateway_id: Optional[str] = None,
        transit_router_attachment_ids: Optional[List[str]] = None
) -> dict[str, Any]:
    """
    调用 describe_transit_router_direct_connect_gateway_attachments 接口，查询满足指定条件的专线网关类型网络实例连接。
    Args:
        transit_router_id (str, optional): 中转路由器实例的ID。
        direct_connect_gateway_id (str, optional): 专线网关实例的ID。
        transit_router_attachment_ids (list[str], optional): 实例连接的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "direct_connect_gateway_id": direct_connect_gateway_id,
        "transit_router_attachment_ids": transit_router_attachment_ids,
    }

    resp = tr_resource.describe_transit_router_direct_connect_gateway_attachments(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_peer_attachment",
    description="创建一个跨地域连接"
)
def create_transit_router_peer_attachment(
        transit_router_id: str = None,
        peer_transit_router_id: str = None,
        peer_transit_router_region_id: str = None,
        transit_router_attachment_name: Optional[str] = None,
        description: Optional[str] = None,
        transit_router_bandwidth_package_id: Optional[int] = None,
        bandwidth: Optional[int] = None,
        tags: Optional[List[Dict[str, str]]] = None,
        client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用CreateTransitRouterPeerAttachment接口，创建一个跨地域连接。
    Args:
        transit_router_id (str): 中转路由器实例ID。
        peer_transit_router_id (str): 对端中转路由器实例ID。
        peer_transit_router_region_id (str): 对端中转路由器所属的地域ID。
        transit_router_attachment_name (str, optional): 中转路由器附件名称。
        description (str, optional): 中转路由器附件的描述信息。
        transit_router_bandwidth_package_id (str, optional): 中转路由器带宽包的ID。
        bandwidth (int, optional): 跨地域连接的带宽，单位为Mbps。
        tags (List[Dict[str, str]], optional): 标签信息列表。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的跨地域连接信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "peer_transit_router_id": peer_transit_router_id,
        "peer_transit_router_region_id": peer_transit_router_region_id,
        "transit_router_attachment_name": transit_router_attachment_name,
        "description": description,
        "tags": tags,
        "transit_router_bandwidth_package_id": transit_router_bandwidth_package_id,
        "bandwidth": bandwidth,
        "client_token": client_token,
    }

    resp = tr_resource.create_transit_router_peer_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_peer_attachments",
    description="查询满足指定条件的跨地域连接"
)
def describe_transit_router_peer_attachments(
        transit_router_id: Optional[str] = None,
        transit_router_attachment_ids: Optional[List[str]] = None,
        peer_transit_router_id: Optional[str] = None,
        peer_transit_router_region_id: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_peer_attachments 查询满足指定条件的跨地域网络实例连接
    Args:
        transit_router_attachment_ids (list[str], optional): 跨地域连接的ID。
        transit_router_id (str, optional): 跨地域连接关联的本端中转路由器实例的ID。
        peer_transit_router_id (str, optional): 对端中转路由器实例的ID。
        peer_transit_router_region_id (str, optional): 对端中转路由器所属地域的ID。
    Returns:
        dict[str, Any]: 跨地域网络实例连接的详细信息。
    """
    req = {
        "transit_router_attachment_ids": transit_router_attachment_ids,
        "transit_router_id": transit_router_id,
        "peer_transit_router_id": peer_transit_router_id,
        "peer_transit_router_region_id": peer_transit_router_region_id,
    }
    resp = tr_resource.describe_transit_router_peer_attachments(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_route_table",
    description="创建一个路由表"
)
def create_transit_router_route_table(
        transit_router_id: str = None,
        transit_router_route_table_name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[Dict[str, str]]] = None,
) -> dict[str, Any]:
    """
    调用CreateTransitRouterRouteTable接口，创建一个路由表。
    Args:
        transit_router_id (str): 中转路由器实例ID。
        transit_router_route_table_name (str, optional): 路由表的名称。
        description (str, optional): 路由表的描述信息。
        tags (List[Dict[str, str]], optional): 标签信息列表。
    Returns:
        dict[str, Any]: 创建的路由表信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_route_table_name": transit_router_route_table_name,
        "description": description,
        "tags": tags,
    }

    resp = tr_resource.create_transit_router_route_table(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_route_tables",
    description="查询满足指定条件的路由表"
)
def describe_transit_router_route_tables(
        transit_router_route_table_ids: Optional[List[str]] = None,
        transit_router_id: str = None,
        transit_router_route_table_type: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_route_tables 查询满足指定条件的路由表
    Args:
        transit_router_route_table_ids (list[str], optional): 路由表的ID列表。
        transit_router_id (str, optional): 路由表关联的本端中转路由器实例的ID。
        transit_router_route_table_type (str, optional): 路由表的类型。
    Returns:
        dict[str, Any]: 路由表的详细信息。
    """
    req = {
        "transit_router_route_table_ids": transit_router_route_table_ids,
        "transit_router_id": transit_router_id,
        "transit_router_route_table_type": transit_router_route_table_type
    }
    resp = tr_resource.describe_transit_router_route_tables(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_route_entry",
    description="创建一条静态路由条目"
)
def create_transit_router_route_entry(
        transit_router_route_table_id: str = None,
        destination_cidr_block: str = None,
        transit_router_route_entry_next_hop_type: str = None,
        transit_router_route_entry_next_hop_id: Optional[str] = None,
        transit_router_route_entry_name: Optional[str] = None,
        description: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用CreateTransitRouterRouteEntry接口，创建一条静态路由条目。
    Args:
        transit_router_route_table_id (str): 路由表的ID。
        destination_cidr_block (str): 路由条目的目标网段。
        transit_router_route_entry_next_hop_type (str): 下一跳类型。
        transit_router_route_entry_next_hop_id (str, optional): 下一跳ID。
        transit_router_route_entry_name (str, optional): 路由条目的名称。
        description (str, optional): 路由条目的描述信息。
    Returns:
        dict[str, Any]: 创建的路由条目信息。
    """
    req = {
        "transit_router_route_table_id": transit_router_route_table_id,
        "destination_cidr_block": destination_cidr_block,
        "transit_router_route_entry_next_hop_type": transit_router_route_entry_next_hop_type,
        "transit_router_route_entry_next_hop_id": transit_router_route_entry_next_hop_id,
        "transit_router_route_entry_name": transit_router_route_entry_name,
        "description": description,
    }

    resp = tr_resource.create_transit_router_route_entry(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_route_entries",
    description="查询满足指定条件的路由条目"
)
def describe_transit_router_route_entries(
    transit_router_route_entry_type: Optional[str] = None,
    transit_router_route_entry_next_hop_type: Optional[str] = None,
    transit_router_route_entry_next_hop_resource_type: Optional[str] = None,
    transit_router_route_table_id: str = None,
    destination_cidr_block: Optional[str] = None,
    status: Optional[str] = None,
    transit_router_route_entry_name: Optional[str] = None,
    transit_router_route_entry_ids: Optional[List[str]] = None
) -> dict[str, Any]:
    """
    调用 describe_transit_router_route_entries 查询满足指定条件的路由条目
    Args:
        transit_router_route_entry_type (str, optional): 路由条目类型。
        transit_router_route_entry_next_hop_type (str, optional): 路由条目的下一跳类型。
        transit_router_route_entry_next_hop_resource_type (str, optional): 路由条目的下一跳资源类型。
        transit_router_route_table_id (str, optional): 路由表的ID。
        destination_cidr_block (str, optional): 路由条目的目标网段。
        status (str, optional): 路由条目的状态。
        transit_router_route_entry_name (str, optional): 路由条目的名称。
        transit_router_route_entry_ids (list[str], optional): 路由条目的ID列表。
    Returns:
        dict[str, Any]: 路由条目的详细信息。
    """
    req = {
        "transit_router_route_entry_type": transit_router_route_entry_type,
        "transit_router_route_entry_next_hop_type": transit_router_route_entry_next_hop_type,
        "transit_router_route_entry_next_hop_resource_type": transit_router_route_entry_next_hop_resource_type,
        "transit_router_route_table_id": transit_router_route_table_id,
        "destination_cidr_block": destination_cidr_block,
        "status": status,
        "transit_router_route_entry_name": transit_router_route_entry_name,
        "transit_router_route_entry_ids": transit_router_route_entry_ids,
    }
    resp = tr_resource.describe_transit_router_route_entries(req)
    return resp.to_dict()

@mcp.tool(
    name="associate_transit_router_attachment_to_route_table",
    description="为指定的网络实例连接关联路由表"
)
def associate_transit_router_attachment_to_route_table(
        transit_router_attachment_id: str = None,
        transit_router_route_table_id: str = None,
) -> dict[str, Any]:
    """
    调用AssociateTransitRouterAttachmentToRouteTable接口，为指定的网络实例连接关联路由表。
    Args:
        transit_router_attachment_id (str): 网络实例连接的ID。
        transit_router_route_table_id (str): 路由表的ID。
    Returns:
        dict[str, Any]: 关联结果信息。
    """
    req = {
        "transit_router_attachment_id": transit_router_attachment_id,
        "transit_router_route_table_id": transit_router_route_table_id,
    }

    resp = tr_resource.associate_transit_router_attachment_to_route_table(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_route_table_associations",
    description="查询满足指定条件的关联转发"
)
def describe_transit_router_route_table_associations(
    transit_router_route_table_id: str = None,
    transit_router_attachment_id: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_route_table_associations 查询满足指定条件的关联转发
    Args:
        transit_router_route_table_id (str, optional): 关联转发关联的路由表实例的ID。
        transit_router_attachment_id (str, optional): 关联转发关联的本端关联实例的ID。
    Returns:
        dict[str, Any]: 关联转发的详细信息。
    """
    req = {
        "transit_router_route_table_id": transit_router_route_table_id,
        "transit_router_attachment_id": transit_router_attachment_id,
    }
    resp = tr_resource.describe_transit_router_route_table_associations(req)
    return resp.to_dict()

@mcp.tool(
    name="enable_transit_router_route_table_propagation",
    description="为指定的网络实例连接启用路由传播"
)
def enable_transit_router_route_table_propagation(
        transit_router_attachment_id: str = None,
        transit_router_route_table_id: str = None,
) -> dict[str, Any]:
    """
    调用EnableTransitRouterRouteTablePropagation接口，为指定的网络实例连接启用路由传播。
    Args:
        transit_router_attachment_id (str): 网络实例连接的ID。
        transit_router_route_table_id (str): 路由表的ID。
    Returns:
        dict[str, Any]: 启用结果信息。
    """
    req = {
        "transit_router_attachment_id": transit_router_attachment_id,
        "transit_router_route_table_id": transit_router_route_table_id,
    }

    resp = tr_resource.enable_transit_router_route_table_propagation(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_route_table_propagations",
    description="查询满足指定条件的路由表传播"
)
def describe_transit_router_route_table_propagations(
        transit_router_route_table_id: str = None,
        transit_router_attachment_id: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_route_table_propagations 查询满足指定条件的路由表传播
    Args:
        transit_router_route_table_id (str, optional): 路由表传播关联的路由表实例的ID。
        transit_router_attachment_id (str, optional): 路由表传播关联的本端关联实例的ID。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_route_table_id": transit_router_route_table_id,
        "transit_router_attachment_id": transit_router_attachment_id,
    }
    resp = tr_resource.describe_transit_router_route_table_propagations(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_route_policy_table",
    description="创建路由策略"
)
def create_transit_router_route_policy_table(
    transit_router_id: str,
    transit_router_route_policy_table_name: Optional[str] = None,
    direction: str = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 create_transit_router_route_policy_table 创建路由策略
    Args:
        transit_router_id (str): 中转路由器实例ID
        transit_router_route_policy_table_name (str, optional): 路由策略名称
        direction (str): 路由策略方向
        description (str, optional): 路由策略描述
        client_token (str, optional): 客户端token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的路由策略信息
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_route_policy_table_name": transit_router_route_policy_table_name,
        "direction": direction,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_route_policy_table(req)
    return resp.to_dict()

@mcp.tool(
    name="associate_transit_router_route_policy_to_route_table",
    description="关联路由策略到路由表"
)
def associate_transit_router_route_policy_to_route_table(
    transit_router_route_table_id: str,
    transit_router_route_policy_table_id: str,
) -> dict[str, Any]:
    """
    调用 associate_transit_router_route_policy_to_route_table 关联路由策略到路由表
    Args:
        transit_router_route_table_id (str): 路由表ID
        transit_router_route_policy_table_id (str): 路由策略ID
    Returns:
        dict[str, Any]: 关联结果信息
    """
    req = {
        "transit_router_route_table_id": transit_router_route_table_id,
        "transit_router_route_policy_table_id": transit_router_route_policy_table_id,
    }
    resp = tr_resource.associate_transit_router_route_policy_to_route_table(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_route_policy_tables",
    description="查询满足指定条件的路由策略。"
)
def describe_transit_router_route_policy_tables(
    transit_router_id: str = None,
    transit_router_route_policy_table_ids: Optional[List[str]] = None,
    transit_router_route_policy_table_name: Optional[str] = None,
    direction: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_route_policy_tables 查询满足指定条件的路由策略。
    Args:
        transit_router_id (str, optional): 路由策略实例的ID列表。
        transit_router_route_policy_table_ids (list[str], optional): 路由策略实例的ID列表。
        transit_router_route_policy_table_name (str, optional): 路由策略实例的名称。
        direction (str, optional): 路由策略的作用方向。
    Returns:
        dict[str, Any]: 路由策略的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_route_policy_table_ids": transit_router_route_policy_table_ids,
        "transit_router_route_policy_table_name": transit_router_route_policy_table_name,
        "direction": direction,
    }
    resp = tr_resource.describe_transit_router_route_policy_tables(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_route_policy_entry",
    description="创建路由策略条目"
)
def create_transit_router_route_policy_entry(
    transit_router_route_policy_table_id: str,
    priority: int,
    action_result: str,
    ip_prefixes: Optional[List[str]] = None,
    source_resource_types: Optional[List[str]] = None,
    source_resource_ids: Optional[List[str]] = None,
    destination_resource_types: Optional[List[str]] = None,
    destination_resource_ids: Optional[List[str]] = None,
    as_path_operate_mode: Optional[str] = None,
    apply_as_path_values: Optional[List[str]] = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 create_transit_router_route_policy_entry 创建路由策略条目
    Args:
        transit_router_route_policy_table_id (str): 路由策略表ID
        priority (int): 路由策略条目的优先级，取值范围为1～10000。数字越小则优先级越高
        action_result (str): 路由策略条目的策略行为，取值包含Permit和Deny
        ip_prefixes (list[str], optional): 路由策略条目的路由前缀
        source_resource_types (list[str], optional): 路由策略条目的源实例类型
        source_resource_ids (list[str], optional): 路由策略条目的源实例ID
        destination_resource_types (list[str], optional): 路由策略条目的目的实例类型
        destination_resource_ids (list[str], optional): 路由策略条目的目的实例ID
        as_path_operate_mode (str, optional): 路由策略条目的AsPath设置方式，取值包含Additive和Replace
        apply_as_path_values (list[str], optional): 路由策略条目设置的路由AsPath，取值范围为1～4294967295
        description (str, optional): 路由策略条目的描述信息
        client_token (str, optional): 客户端token，用于保证请求的幂等性
    Returns:
        dict[str, Any]: 创建的路由策略条目信息
    """
    req = {
        "transit_router_route_policy_table_id": transit_router_route_policy_table_id,
        "priority": priority,
        "ip_prefixes": ip_prefixes,
        "source_resource_types": source_resource_types,
        "source_resource_ids": source_resource_ids,
        "destination_resource_types": destination_resource_types,
        "destination_resource_ids": destination_resource_ids,
        "action_result": action_result,
        "as_path_operate_mode": as_path_operate_mode,
        "apply_as_path_values": apply_as_path_values,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_route_policy_entry(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_route_policy_entries",
    description="查询满足指定条件的路由策略条目"
)
def describe_transit_router_route_policy_entries(
    transit_router_route_policy_table_id: str = None,
    transit_router_route_policy_entry_ids: Optional[List[str]] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_route_policy_entries 查询满足指定条件的路由策略条目
    Args:
        transit_router_route_policy_table_id (str, optional): 路由策略表ID
        transit_router_route_policy_entry_ids (list[str], optional): 路由策略条目ID列表
    Returns:
        dict[str, Any]: 路由策略条目信息
    """
    req = {
        "transit_router_route_policy_table_id": transit_router_route_policy_table_id,
        "transit_router_route_policy_entry_ids": transit_router_route_policy_entry_ids,
    }
    resp = tr_resource.describe_transit_router_route_policy_entries(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_forward_policy_table",
    description="为指定中转路由器创建一个转发策略"
)
def create_transit_router_forward_policy_table(
    transit_router_id: str,
    transit_router_forward_policy_table_name: Optional[str] = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 create_transit_router_forward_policy_table 为指定中转路由器创建一个转发策略
    Args:
        transit_router_id (str): 中转路由器ID
        transit_router_forward_policy_table_name (str, optional): 转发策略的名称
        description (str, optional): 转发策略的描述信息
        client_token (str, optional): 客户端token，用于保证请求的幂等性
    Returns:
        dict[str, Any]: 创建的转发策略信息
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_forward_policy_table_name": transit_router_forward_policy_table_name,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_forward_policy_table(req)
    return resp.to_dict()

@mcp.tool(
    name="associate_transit_router_forward_policy_table_to_attachment",
    description="将指定的转发策略绑定至网络实例连接或跨地域连接"
)
def associate_transit_router_forward_policy_table_to_attachment(
    transit_router_attachment_id: str,
    transit_router_forward_policy_table_id: str,
) -> dict[str, Any]:
    """
    调用 associate_transit_router_forward_policy_table_to_attachment 将指定的转发策略绑定至网络实例连接或跨地域连接
    Args:
        transit_router_attachment_id (str): 中转路由器连接ID
        transit_router_forward_policy_table_id (str): 转发策略ID
    Returns:
        dict[str, Any]: 绑定结果
    """
    req = {
        "transit_router_attachment_id": transit_router_attachment_id,
        "transit_router_forward_policy_table_id": transit_router_forward_policy_table_id,
    }
    resp = tr_resource.associate_transit_router_forward_policy_table_to_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_forward_policy_tables",
    description="查询满足指定条件的转发策略"
)
def describe_transit_router_forward_policy_tables(
    transit_router_forward_policy_table_ids: Optional[List[str]] = None,
    transit_router_forward_policy_table_name: Optional[str] = None,
    transit_router_id: str = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_forward_policy_tables 查询满足指定条件的转发策略
    Args:
        transit_router_forward_policy_table_ids (list[str], optional): 路由策略实例的ID列表。
        transit_router_forward_policy_table_name (str, optional): 路由策略实例的名称。
        transit_router_id (str, optional): 路由策略实例的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_forward_policy_table_ids": transit_router_forward_policy_table_ids,
        "transit_router_forward_policy_table_name": transit_router_forward_policy_table_name,
        "transit_router_id": transit_router_id,
    }
    resp = tr_resource.describe_transit_router_forward_policy_tables(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_forward_policy_entry",
    description="为指定的转发策略添加策略条目"
)
def create_transit_router_forward_policy_entry(
    transit_router_forward_policy_table_id: str,
    transit_router_route_table_id: str,
    source_cidr_block: str,
    priority: int,
    destination_cidr_block: Optional[str] = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 create_transit_router_forward_policy_entry 为指定的转发策略添加策略条目
    Args:
        transit_router_forward_policy_table_id (str): 转发策略ID
        transit_router_route_table_id (str): 路由表ID
        source_cidr_block (str): 转发策略条目的源地址段，支持IPv4和IPv6网段
        priority (int): 转发策略条目的优先级，取值范围为1～10000
        destination_cidr_block (str, optional): 转发策略条目的目的地址段，支持IPv4和IPv6网段
        description (str, optional): 转发策略条目的描述信息
        client_token (str, optional): 客户端token，用于保证请求的幂等性
    Returns:
        dict[str, Any]: 创建的转发策略条目信息
    """
    req = {
        "transit_router_forward_policy_table_id": transit_router_forward_policy_table_id,
        "transit_router_route_table_id": transit_router_route_table_id,
        "source_cidr_block": source_cidr_block,
        "priority": priority,
        "destination_cidr_block": destination_cidr_block,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_forward_policy_entry(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_forward_policy_entries",
    description="查询满足指定条件的转发策略条目"
)
def describe_transit_router_forward_policy_entries(
    source_cidr_block: Optional[str] = None,
    destination_cidr_block: Optional[str] = None,
    transit_router_forward_policy_entry_ids: Optional[List[str]] = None,
    transit_router_forward_policy_table_id: str = None,
    transit_router_route_table_id: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_forward_policy_entries 查询满足指定条件的转发策略条目
    Args:
        source_cidr_block (str, optional): 路由策略实例的ID列表。
        destination_cidr_block (list[str], optional): 路由策略实例的ID列表。
        transit_router_forward_policy_entry_ids (str, optional): 路由策略的作用方向。
        transit_router_forward_policy_table_id (str, optional): 路由策略实例的ID列表。
        transit_router_route_table_id (str, optional): 路由策略实例的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "source_cidr_block": source_cidr_block,
        "destination_cidr_block": destination_cidr_block,
        "transit_router_forward_policy_entry_ids": transit_router_forward_policy_entry_ids,
        "transit_router_forward_policy_table_id": transit_router_forward_policy_table_id,
        "transit_router_route_table_id": transit_router_route_table_id,
    }
    resp = tr_resource.describe_transit_router_forward_policy_entries(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_traffic_qos_marking_policies",
    description="查询满足指定条件的流标记策略"
)
def describe_transit_router_traffic_qos_marking_policies(
    transit_router_traffic_qos_marking_policy_ids: Optional[List[str]] = None,
    transit_router_traffic_qos_marking_policy_name: Optional[List[str]] = None,
    transit_router_id: str = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_traffic_qos_marking_policies 查询满足指定条件的流标记策略
    Args:
        transit_router_traffic_qos_marking_policy_ids (list[str], optional): 流标记策略的ID。
        transit_router_traffic_qos_marking_policy_name (str, optional): 路由策略实例的名称。
        transit_router_id (str, optional): 路由策略实例的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_traffic_qos_marking_policy_ids": transit_router_traffic_qos_marking_policy_ids,
        "transit_router_traffic_qos_marking_policy_name": transit_router_traffic_qos_marking_policy_name,
        "transit_router_id": transit_router_id,
    }
    resp = tr_resource.describe_transit_router_traffic_qos_marking_policies(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_traffic_qos_marking_entries",
    description="查询流标记策略中满足指定条件的标记规则。"
)
def describe_transit_router_traffic_qos_marking_entries(
    transit_router_traffic_qos_marking_policy_id: str = None,
    transit_router_traffic_qos_marking_entry_ids: Optional[List[str]] = None,
    transit_router_traffic_qos_marking_entry_name: Optional[str] = None,
    protocol: Optional[str] = None,
    source_cidr_block: Optional[str] = None,
    destination_cidr_block: Optional[str] = None,
    match_dscp: Optional[str] = None,
    remarking_dscp: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_traffic_qos_marking_entries 查询流标记策略中满足指定条件的标记规则。
    Args:
        transit_router_traffic_qos_marking_policy_id (str, optional): 流量标记策略实例的ID。
        transit_router_traffic_qos_marking_entry_ids (list[str], optional): 流量标记条目的ID列表。
        transit_router_traffic_qos_marking_entry_name (str, optional): 流量标记条目的名称。
        protocol (str, optional): 流量标记条目的协议。
        source_cidr_block (str, optional): 流量标记条目的源IP地址范围。
        destination_cidr_block (str, optional): 流量标记条目的目标IP地址范围。
        match_dscp (str, optional): 流量标记条目的DSCP值。
        remarking_dscp (str, optional): 流量标记条目的重写DSCP值。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_traffic_qos_marking_policy_id": transit_router_traffic_qos_marking_policy_id,
        "transit_router_traffic_qos_marking_entry_ids": transit_router_traffic_qos_marking_entry_ids,
        "transit_router_traffic_qos_marking_entry_name": transit_router_traffic_qos_marking_entry_name,
        "protocol": protocol,
        "source_cidr_block": source_cidr_block,
        "destination_cidr_block": destination_cidr_block,
        "match_dscp": match_dscp,
        "remarking_dscp": remarking_dscp,
    }
    resp = tr_resource.describe_transit_router_traffic_qos_marking_entries(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_traffic_qos_marking_policy",
    description="创建流标记策略"
)
def create_transit_router_traffic_qos_marking_policy(
    transit_router_id: str,
    transit_router_traffic_qos_marking_policy_name: Optional[str] = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterTrafficQosMarkingPolicy 接口，创建流标记策略。
    Args:
        transit_router_id (str): 中转路由器实例的ID。
        transit_router_traffic_qos_marking_policy_name (str, optional): 流标记策略的名称。
        description (str, optional): 流标记策略的描述信息。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的流标记策略信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_traffic_qos_marking_policy_name": transit_router_traffic_qos_marking_policy_name,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_traffic_qos_marking_policy(req)
    return resp.to_dict()

@mcp.tool(
    name="associate_transit_router_traffic_qos_marking_policy_to_attachment",
    description="绑定流标记策略至TR连接"
)
def associate_transit_router_traffic_qos_marking_policy_to_attachment(
    transit_router_attachment_id: str,
    transit_router_traffic_qos_marking_policy_id: str
) -> dict[str, Any]:
    """
    调用 AssociateTransitRouterTrafficQosMarkingPolicyToAttachment 接口，绑定流标记策略至TR连接。
    Args:
        transit_router_attachment_id (str): TR连接的ID。
        transit_router_traffic_qos_marking_policy_id (str): 流标记策略的ID。
    Returns:
        dict[str, Any]: 绑定结果。
    """
    req = {
        "transit_router_attachment_id": transit_router_attachment_id,
        "transit_router_traffic_qos_marking_policy_id": transit_router_traffic_qos_marking_policy_id,
    }
    resp = tr_resource.associate_transit_router_traffic_qos_marking_policy_to_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_traffic_qos_marking_entry",
    description="添加流标记规则"
)
def create_transit_router_traffic_qos_marking_entry(
    transit_router_traffic_qos_marking_policy_id: str,
    priority: int,
    source_cidr_block: str,
    destination_cidr_block: str,
    source_port_start: int,
    source_port_end: int,
    destination_port_start: int,
    destination_port_end: int,
    remarking_dscp: int,
    protocol: Optional[str] = None,
    match_dscp: Optional[int] = None,
    transit_router_traffic_qos_marking_entry_name: Optional[str] = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterTrafficQosMarkingEntry 接口，为流标记策略添加标记规则。
    Args:
        transit_router_traffic_qos_marking_policy_id (str): 流标记策略的ID。
        priority (int): 标记规则的优先级，取值范围为1～10000。
        source_cidr_block (str): 源地址的IP网段。
        destination_cidr_block (str): 目的地址的IP网段。
        source_port_start (int): 源端口范围的起始值。
        source_port_end (int): 源端口范围的结束值。
        destination_port_start (int): 目的端口范围的起始值。
        destination_port_end (int): 目的端口范围的结束值。
        remarking_dscp (int): 为目标流量报文修改的DSCP值，取值范围为0～63。
        protocol (str, optional): 协议类型。
        match_dscp (int, optional): 流量报文本身的DSCP值。
        transit_router_traffic_qos_marking_entry_name (str, optional): 标记规则的名称。
        description (str, optional): 标记规则的描述信息。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的标记规则信息。
    """
    req = {
        "transit_router_traffic_qos_marking_policy_id": transit_router_traffic_qos_marking_policy_id,
        "priority": priority,
        "source_cidr_block": source_cidr_block,
        "destination_cidr_block": destination_cidr_block,
        "source_port_start": source_port_start,
        "source_port_end": source_port_end,
        "destination_port_start": destination_port_start,
        "destination_port_end": destination_port_end,
        "remarking_dscp": remarking_dscp,
        "protocol": protocol,
        "match_dscp": match_dscp,
        "transit_router_traffic_qos_marking_entry_name": transit_router_traffic_qos_marking_entry_name,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_traffic_qos_marking_entry(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_traffic_qos_queue_policy",
    description="创建流队列策略"
)
def create_transit_router_traffic_qos_queue_policy(
    transit_router_id: str,
    transit_router_traffic_qos_queue_policy_name: Optional[str] = None,
    description: Optional[str] = None,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterTrafficQosQueuePolicy 接口，创建一个流队列策略。
    Args:
        transit_router_id (str): 中转路由器实例的ID。
        transit_router_traffic_qos_queue_policy_name (str, optional): 流队列策略的名称。
        description (str, optional): 流队列策略的描述信息。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的流队列策略信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_traffic_qos_queue_policy_name": transit_router_traffic_qos_queue_policy_name,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_traffic_qos_queue_policy(req)
    return resp.to_dict()

@mcp.tool(
    name="associate_transit_router_traffic_qos_queue_policy_to_attachment",
    description="绑定流队列策略至TR连接"
)
def associate_transit_router_traffic_qos_queue_policy_to_attachment(
    transit_router_attachment_id: str,
    transit_router_traffic_qos_queue_policy_id: str
) -> dict[str, Any]:
    """
    调用 AssociateTransitRouterTrafficQosQueuePolicyToAttachment 接口，绑定流队列策略至TR连接。
    Args:
        transit_router_attachment_id (str): TR连接的ID。
        transit_router_traffic_qos_queue_policy_id (str): 流队列策略的ID。
    Returns:
        dict[str, Any]: 绑定结果。
    """
    req = {
        "transit_router_attachment_id": transit_router_attachment_id,
        "transit_router_traffic_qos_queue_policy_id": transit_router_traffic_qos_queue_policy_id,
    }
    resp = tr_resource.associate_transit_router_traffic_qos_queue_policy_to_attachment(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_traffic_qos_queue_entry",
    description="添加流队列"
)
def create_transit_router_traffic_qos_queue_entry(
    transit_router_traffic_qos_queue_policy_id: str,
    dscps: List[int],
    bandwidth_percent: int,
    transit_router_traffic_qos_queue_entry_name: str,
    description: Optional[str] = None,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterTrafficQosQueueEntry 接口，为流队列策略添加队列。
    Args:
        transit_router_traffic_qos_queue_policy_id (str): 流队列策略的ID。
        dscps (List[int]): 队列需要匹配的DSCP值，取值范围为0～63。
        bandwidth_percent (int): 队列可使用的跨地域带宽的百分比，取值范围为0～100。
        transit_router_traffic_qos_queue_entry_name (str): 队列的名称。
        description (str, optional): 队列的描述信息。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的流队列信息。
    """
    req = {
        "transit_router_traffic_qos_queue_policy_id": transit_router_traffic_qos_queue_policy_id,
        "dscps": dscps,
        "bandwidth_percent": bandwidth_percent,
        "transit_router_traffic_qos_queue_entry_name": transit_router_traffic_qos_queue_entry_name,
        "description": description,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_traffic_qos_queue_entry(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_traffic_qos_queue_policies",
    description="查询满足指定条件的流量调度策略。"
)
def describe_transit_router_traffic_qos_queue_policies(
    transit_router_id: str = None,
    transit_router_traffic_qos_queue_policy_ids: Optional[List[str]] = None,
    transit_router_traffic_qos_queue_policy_name: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_traffic_qos_queue_policies 查询满足指定条件的流量调度策略。
    Args:
        transit_router_id (str, optional): 流量调度策略实例的ID。
        transit_router_traffic_qos_queue_policy_ids (list[str], optional): 流量调度策略实例的ID列表。
        transit_router_traffic_qos_queue_policy_name (str, optional): 流量调度策略实例的名称。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_traffic_qos_queue_policy_ids": transit_router_traffic_qos_queue_policy_ids,
        "transit_router_traffic_qos_queue_policy_name": transit_router_traffic_qos_queue_policy_name,
    }
    resp = tr_resource.describe_transit_router_traffic_qos_queue_policies(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_traffic_qos_queue_entries",
    description="查询满足指定条件的流队列。"
)
def describe_transit_router_traffic_qos_queue_entries(
    transit_router_traffic_qos_queue_policy_id: str = None,
    transit_router_traffic_qos_queue_entry_ids: Optional[List[str]] = None,
    transit_router_traffic_qos_queue_entry_name: Optional[str] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_traffic_qos_queue_entries 查询满足指定条件的流队列。
    Args:
        transit_router_traffic_qos_queue_policy_id (str, optional): 流量调度策略实例的ID。
        transit_router_traffic_qos_queue_entry_ids (list[str], optional): 流量调度队列实例的ID列表。
        transit_router_traffic_qos_queue_entry_name (str, optional): 流量调度队列实例的名称。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_traffic_qos_queue_policy_id": transit_router_traffic_qos_queue_policy_id,
        "transit_router_traffic_qos_queue_entry_ids": transit_router_traffic_qos_queue_entry_ids,
        "transit_router_traffic_qos_queue_entry_name": transit_router_traffic_qos_queue_entry_name,
    }
    resp = tr_resource.describe_transit_router_traffic_qos_queue_entries(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_regions",
    description="查询中转路由器地域信息"
)
def describe_transit_router_regions(
        geographic_region_set_id: Optional[str] = None,
        region_ids: Optional[List[str]] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_regions 接口，查询中转路由器地域信息
    Args:
        geographic_region_set_id (str, optional): 地域集合的ID。
        region_ids (list[str], optional): 地域实例的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "geographic_region_set_id": geographic_region_set_id,
        "region_ids": region_ids,
    }
    resp = tr_resource.describe_transit_router_regions(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_bandwidth_packages",
    description="查询满足指定条件的中转路由器带宽包。"
)
def describe_transit_router_bandwidth_packages(
        transit_router_bandwidth_package_ids: Optional[List[str]] = None,
        local_geographic_region_set_id: Optional[str] = None,
        peer_geographic_region_set_id: Optional[str] = None,
        transit_router_peer_attachment_id: Optional[str] = None,
        transit_router_bandwidth_package_name: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 describe_transit_router_bandwidth_packages 接口，查询中转路由器带宽包列表
    Args:
        transit_router_bandwidth_package_ids (list[str], optional): 实例连接的ID列表。
        local_geographic_region_set_id (str, optional): 本地地域集合的ID。
        peer_geographic_region_set_id (str, optional): 对等地域集合的ID。
        transit_router_peer_attachment_id (str, optional): 对等连接实例的ID。
        transit_router_bandwidth_package_name (str, optional): 带宽包实例的名称。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_bandwidth_package_ids": transit_router_bandwidth_package_ids,
        "local_geographic_region_set_id": local_geographic_region_set_id,
        "peer_geographic_region_set_id": peer_geographic_region_set_id,
        "transit_router_peer_attachment_id": transit_router_peer_attachment_id,
        "transit_router_bandwidth_package_name": transit_router_bandwidth_package_name,
    }
    resp = tr_resource.describe_transit_router_bandwidth_packages(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_bandwidth_packages_billing",
    description="查询中转路由器带宽包计费方式列表"
)
def describe_transit_router_bandwidth_packages_billing(
        transit_router_bandwidth_package_ids: Optional[List[str]] = None,
) -> dict[str, Any]:
    """
    调用 describe_transit_router_bandwidth_packages_billing 查询中转路由器带宽包计费方式列表
    Args:
        transit_router_bandwidth_package_ids (list[str], optional): 实例连接的ID列表。
    Returns:
        dict[str, Any]: 实例共享的详细信息。
    """
    req = {
        "transit_router_bandwidth_package_ids": transit_router_bandwidth_package_ids,
    }
    resp = tr_resource.describe_transit_router_bandwidth_packages_billing(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_multicast_domain",
    description="创建组播域"
)
def create_transit_router_multicast_domain(
    transit_router_id: str,
    transit_router_multicast_domain_name: Optional[str] = None,
    description: Optional[str] = None,
    tags: Optional[List[Dict[str, str]]] = None,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterMulticastDomain 接口，为指定中转路由器创建一个组播域。
    Args:
        transit_router_id (str): 中转路由器实例的ID。
        transit_router_multicast_domain_name (str, optional): 组播域的名称。
        description (str, optional): 组播域的描述信息。
        tags (List[Dict[str, str]], optional): 用户标签的标签键和标签值。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的组播域信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_multicast_domain_name": transit_router_multicast_domain_name,
        "description": description,
        "tags": tags,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_multicast_domain(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_multicast_domains",
    description="查询组播域列表"
)
def describe_transit_router_multicast_domains(
    transit_router_id: str,
    transit_router_multicast_domain_ids: Optional[List[str]] = None,
    transit_router_multicast_domain_name: Optional[str] = None,
    tag_filters: Optional[List[Dict[str, List[str]]]] = None,
    page_number: Optional[int] = None,
    page_size: Optional[int] = None
) -> dict[str, Any]:
    """
    调用 DescribeTransitRouterMulticastDomains 接口，查询满足指定条件的组播域列表。
    Args:
        transit_router_id (str): 中转路由器实例的ID。
        transit_router_multicast_domain_ids (List[str], optional): 组播域的ID列表。
        transit_router_multicast_domain_name (str, optional): 组播域的名称。
        tag_filters (List[Dict[str, List[str]]], optional): 标签过滤条件。
        page_number (int, optional): 列表的页码。
        page_size (int, optional): 分页查询时每页的行数。
    Returns:
        dict[str, Any]: 组播域的详细信息。
    """
    req = {
        "transit_router_id": transit_router_id,
        "transit_router_multicast_domain_ids": transit_router_multicast_domain_ids,
        "transit_router_multicast_domain_name": transit_router_multicast_domain_name,
        "tag_filters": tag_filters,
        "page_number": page_number,
        "page_size": page_size,
    }
    resp = tr_resource.describe_transit_router_multicast_domains(req)
    return resp.to_dict()

@mcp.tool(
    name="associate_transit_router_multicast_domain",
    description="组播域关联子网"
)
def associate_transit_router_multicast_domain(
    transit_router_multicast_domain_id: str,
    transit_router_attachment_id: str,
    subnet_id: str
) -> dict[str, Any]:
    """
    调用 AssociateTransitRouterMulticastDomain 接口，将组播域关联至指定子网。
    Args:
        transit_router_multicast_domain_id (str): 组播域的ID。
        transit_router_attachment_id (str): 网络实例连接的ID。
        subnet_id (str): 子网的ID。
    Returns:
        dict[str, Any]: 关联结果。
    """
    req = {
        "transit_router_multicast_domain_id": transit_router_multicast_domain_id,
        "transit_router_attachment_id": transit_router_attachment_id,
        "subnet_id": subnet_id,
    }
    resp = tr_resource.associate_transit_router_multicast_domain(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_multicast_domain_associations",
    description="查询组播域关联关系"
)
def describe_transit_router_multicast_domain_associations(
    transit_router_multicast_domain_id: Optional[str] = None,
    transit_router_attachment_id: Optional[str] = None,
    subnet_ids: Optional[List[str]] = None,
    resource_type: Optional[str] = None,
    resource_id: Optional[str] = None,
    page_number: Optional[int] = None,
    page_size: Optional[int] = None
) -> dict[str, Any]:
    """
    调用 DescribeTransitRouterMulticastDomainAssociations 接口，查询满足指定条件的组播域的关联信息。
    Args:
        transit_router_multicast_domain_id (str, optional): 组播域的ID。
        transit_router_attachment_id (str, optional): 网络实例连接的ID。
        subnet_ids (List[str], optional): 子网的ID列表。
        resource_type (str, optional): 网络实例的类型。
        resource_id (str, optional): 组播资源的ID。
        page_number (int, optional): 列表的页码。
        page_size (int, optional): 分页查询时每页的行数。
    Returns:
        dict[str, Any]: 组播域关联关系的详细信息。
    """
    req = {
        "transit_router_multicast_domain_id": transit_router_multicast_domain_id,
        "transit_router_attachment_id": transit_router_attachment_id,
        "subnet_ids": subnet_ids,
        "resource_type": resource_type,
        "resource_id": resource_id,
        "page_number": page_number,
        "page_size": page_size,
    }
    resp = tr_resource.describe_transit_router_multicast_domain_associations(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_multicast_group_member",
    description="创建组播组成员"
)
def create_transit_router_multicast_group_member(
    transit_router_multicast_domain_id: str,
    group_ip_address: str,
    network_interface_id: str,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterMulticastGroupMember 接口，为指定的组播域添加组播成员。
    Args:
        transit_router_multicast_domain_id (str): 组播域的ID。
        group_ip_address (str): 组播组的IP地址。取值范围为224.0.1.0~239.255.255.254。
        network_interface_id (str): 网卡的ID。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建结果。
    """
    req = {
        "transit_router_multicast_domain_id": transit_router_multicast_domain_id,
        "group_ip_address": group_ip_address,
        "network_interface_id": network_interface_id,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_multicast_group_member(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_multicast_group_source",
    description="创建组播组源"
)
def create_transit_router_multicast_group_source(
    transit_router_multicast_domain_id: str,
    group_ip_address: str,
    network_interface_id: str,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterMulticastGroupSource 接口，为指定的组播域添加组播源。
    Args:
        transit_router_multicast_domain_id (str): 组播域的ID。
        group_ip_address (str): 组播组的IP地址。取值范围为224.0.1.0~239.255.255.254。
        network_interface_id (str): 网卡的ID。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建结果。
    """
    req = {
        "transit_router_multicast_domain_id": transit_router_multicast_domain_id,
        "group_ip_address": group_ip_address,
        "network_interface_id": network_interface_id,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_multicast_group_source(req)
    return resp.to_dict()

@mcp.tool(
    name="describe_transit_router_multicast_groups",
    description="查询组播组列表"
)
def describe_transit_router_multicast_groups(
    transit_router_multicast_domain_id: Optional[str] = None,
    group_ip_address: Optional[str] = None,
    transit_router_attachment_id: Optional[str] = None,
    resource_type: Optional[str] = None,
    resource_id: Optional[str] = None,
    subnet_ids: Optional[List[str]] = None,
    network_interface_ids: Optional[List[str]] = None,
    is_group_source: Optional[bool] = None,
    is_group_member: Optional[bool] = None,
    source_type: Optional[str] = None,
    member_type: Optional[str] = None,
    page_number: Optional[int] = None,
    page_size: Optional[int] = None
) -> dict[str, Any]:
    """
    调用 DescribeTransitRouterMulticastGroups 接口，查询指定组播域中的组播源和组播成员。
    Args:
        transit_router_multicast_domain_id (str, optional): 组播域的ID。
        group_ip_address (str, optional): 组播组的IP地址。取值范围为224.0.1.0~239.255.255.254。
        transit_router_attachment_id (str, optional): 网络实例连接的ID。
        resource_type (str, optional): 组播资源的类型。VPC：私有网络。
        resource_id (str, optional): 组播资源的ID。
        subnet_ids (List[str], optional): 子网的ID列表。
        network_interface_ids (List[str], optional): 网卡的ID列表。
        is_group_source (bool, optional): 是否查询组播源。
        is_group_member (bool, optional): 是否查询组播成员。
        source_type (str, optional): 组播源的类型。Static：静态组播源。
        member_type (str, optional): 组播成员的类型。Static：静态组播成员。
        page_number (int, optional): 列表的页码，默认值为1。
        page_size (int, optional): 分页查询时每页的行数，取值范围为1 ~ 100，默认值为20。
    Returns:
        dict[str, Any]: 组播组的详细信息。
    """
    req = {
        "transit_router_multicast_domain_id": transit_router_multicast_domain_id,
        "group_ip_address": group_ip_address,
        "transit_router_attachment_id": transit_router_attachment_id,
        "resource_type": resource_type,
        "resource_id": resource_id,
        "subnet_ids": subnet_ids,
        "network_interface_ids": network_interface_ids,
        "is_group_source": is_group_source,
        "is_group_member": is_group_member,
        "source_type": source_type,
        "member_type": member_type,
        "page_number": page_number,
        "page_size": page_size,
    }
    resp = tr_resource.describe_transit_router_multicast_groups(req)
    return resp.to_dict()

@mcp.tool(
    name="create_transit_router_bandwidth_package",
    description="创建中转路由器带宽包"
)
def create_transit_router_bandwidth_package(
    local_geographic_region_set_id: str,
    peer_geographic_region_set_id: str,
    line_operator: Optional[str] = None,
    bandwidth: Optional[int] = None,
    transit_router_bandwidth_package_name: Optional[str] = None,
    description: Optional[str] = None,
    billing_type: Optional[int] = None,
    period_unit: Optional[str] = None,
    period: Optional[int] = None,
    project_name: Optional[str] = None,
    tags: Optional[List[Dict[str, str]]] = None,
    client_token: Optional[str] = None
) -> dict[str, Any]:
    """
    调用 CreateTransitRouterBandwidthPackage 接口，创建一个中转路由器带宽包，用于为跨地域互通提供带宽。
    Args:
        local_geographic_region_set_id (str): 中转路由器带宽包互通的本端地理区域ID。取值如下：China：中国大陆。Asia：亚太。
        peer_geographic_region_set_id (str): 中转路由器带宽包互通的对端地理区域ID。取值如下：China：中国大陆。Asia：亚太。
        line_operator (str, optional): 跨境带宽包线路运营商。ChinaUnicom（默认值）：中国联通。ChinaTelecom：中国电信。
        bandwidth (int, optional): 中转路由器带宽包的带宽峰值。取值范围为2 ~ 10000，单位为Mbps，默认值为2Mbps。
        transit_router_bandwidth_package_name (str, optional): 中转路由器带宽包的名称。
        description (str, optional): 中转路由器带宽包的描述。
        billing_type (int, optional): 中转路由器带宽包的计费方式。取值如下：1（默认值）：包年包月。
        period_unit (str, optional): 中转路由器带宽包的计费周期。取值如下：Month（默认值）：按月计费。Year：按年计费。
        period (int, optional): 中转路由器带宽包的购买时长，默认值为1。
        project_name (str, optional): 中转路由器带宽包所属项目的名称。
        tags (List[Dict[str, str]], optional): 用户标签的标签键和标签值。
        client_token (str, optional): 客户端Token，用于保证请求的幂等性。
    Returns:
        dict[str, Any]: 创建的带宽包信息。
    """
    req = {
        "local_geographic_region_set_id": local_geographic_region_set_id,
        "peer_geographic_region_set_id": peer_geographic_region_set_id,
        "line_operator": line_operator,
        "bandwidth": bandwidth,
        "transit_router_bandwidth_package_name": transit_router_bandwidth_package_name,
        "description": description,
        "billing_type": billing_type,
        "period_unit": period_unit,
        "period": period,
        "project_name": project_name,
        "tags": tags,
        "client_token": client_token,
    }
    resp = tr_resource.create_transit_router_bandwidth_package(req)
    return resp.to_dict()

@mcp.tool(
    name="renew_transit_router_bandwidth_package",
    description="续费中转路由器带宽包"
)
def renew_transit_router_bandwidth_package(
    transit_router_bandwidth_package_id: str,
    period_unit: Optional[str] = None,
    period: Optional[int] = None
) -> dict[str, Any]:
    """
    调用 RenewTransitRouterBandwidthPackage 接口，为包年包月类型的中转路由器带宽包续期。
    Args:
        transit_router_bandwidth_package_id (str): 中转路由器带宽包的ID。
        period_unit (str, optional): 中转路由器带宽包的计费周期。取值如下：Month（默认值）：按月计费。Year：按年计费。
        period (int, optional): 中转路由器带宽包的购买时长，默认值为1。当PeriodUnit取值为"Month"时，取值为1～9，12，24和36。当PeriodUnit取值为"Year"时，取值为1～3。
    Returns:
        dict[str, Any]: 续费结果。
    """
    req = {
        "transit_router_bandwidth_package_id": transit_router_bandwidth_package_id,
        "period_unit": period_unit,
        "period": period,
    }
    resp = tr_resource.renew_transit_router_bandwidth_package(req)
    return resp.to_dict()

@mcp.tool(
    name="set_transit_router_bandwidth_package_renewal",
    description="设置中转路由器带宽包续费类型"
)
def set_transit_router_bandwidth_package_renewal(
    transit_router_bandwidth_package_id: str,
    renew_type: str,
    renew_period: Optional[int] = None,
    remain_renew_times: Optional[int] = None
) -> dict[str, Any]:
    """
    调用 SetTransitRouterBandwidthPackageRenewal 接口，设置包年包月类型中转路由器带宽包的续费类型。
    Args:
        transit_router_bandwidth_package_id (str): 带宽包实例的ID。
        renew_type (str): 中转路由器带宽包的续费类型。取值如下：Manual：手动续费。Auto：自动续费。NoRenew：不续费。
        renew_period (int, optional): 单次自动续费的时长，单位为月。取值包括1～3，6和12，默认值为1。当RenewType配置为Auto时生效。
        remain_renew_times (int, optional): 自动续费的次数。取值包括-1和1～100，默认值为-1，表示自动续费无限次。当RenewType配置为Auto时生效。
    Returns:
        dict[str, Any]: 设置结果。
    """
    req = {
        "transit_router_bandwidth_package_id": transit_router_bandwidth_package_id,
        "renew_type": renew_type,
        "renew_period": renew_period,
        "remain_renew_times": remain_renew_times,
    }
    resp = tr_resource.set_transit_router_bandwidth_package_renewal(req)
    return resp.to_dict()


if __name__ == "__main__":
    mcp.run()
