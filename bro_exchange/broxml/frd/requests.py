from lxml import etree
from abc import ABC, abstractmethod

import bro_exchange.broxml.frd.constructables as constructables
from bro_exchange.broxml.mappings import (
    frd_namespaces,
    frd_nsmap
)


class FRDRegistrationTool(ABC):
    def __init__(self, srcdocdata: dict) -> None:
        self.srcdocdata = srcdocdata
        self.xml_tree = None
        self.source_document = None
    
    def generate_xml_file(self):
        """
        Generates the XML file, based on the provide sourcedocsdata
        """
        self.setup_xml_tree()
        self.create_sourcedocument()

        self.xml_tree.append(self.source_document)

        self.xml_tree = etree.ElementTree(self.xml_tree)
        
        return self.xml_tree
    
    def setup_xml_tree(self):
        """
        Sets up the basis of a startregistration xml file
        """
        # Setup file
        self.xml_tree = etree.Element(
                "registrationRequest",
                nsmap=frd_namespaces,
            )
        
        self.xml_tree.set(
            "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
            "http://www.broservices.nl/xsd/isfrd/1.0 ../../XSD/isfrd-messages.xsd",
        )

        # add request
        request_reference = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "requestReference",
            nsmap=frd_namespaces,
        )
        request_reference.text = self.srcdocdata["request_reference"]

        # add delivery accountable party
        delivery_accountable_party = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "deliveryAccountableParty",
            nsmap=frd_namespaces,
        )
        delivery_accountable_party.text = self.srcdocdata["delivery_accountable_party"]
        
        # add bro id of the formation resistance dossier
        bro_id = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "broId",
            nsmap=frd_namespaces,
        )
        bro_id.text = self.srcdocdata["bro_id"]

        # add quality regime
        quality_regime = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "qualityRegime",
            nsmap=frd_namespaces,
        )
        quality_regime.text = self.srcdocdata["quality_regime"]

    @abstractmethod
    def create_sourcedocument(self):
        pass

class FRDReplaceTool(ABC):
    def __init__(self, srcdocdata: dict) -> None:
        self.srcdocdata = srcdocdata
        self.xml_tree = None
        self.source_document = None
    
    def generate_xml_file(self):
        """
        Generates the XML file, based on the provide sourcedocsdata
        """
        self.setup_xml_tree()
        self.create_sourcedocument()

        self.xml_tree.append(self.source_document)

        self.xml_tree = etree.ElementTree(self.xml_tree)
        
        return self.xml_tree
    
    def setup_xml_tree(self):
        """
        Sets up the basis of a replace request xml file
        """
        
        # Setup file
        self.xml_tree = etree.Element(
                "replaceRequest",
                nsmap=frd_namespaces,
            )
        
        self.xml_tree.set(
            "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
            "http://www.broservices.nl/xsd/isfrd/1.0 ../../XSD/isfrd-messages.xsd",
        )

        # add request
        request_reference = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "requestReference",
            nsmap=frd_namespaces,
        )
        request_reference.text = self.srcdocdata["request_reference"]

        # add delivery accountable party
        delivery_accountable_party = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "deliveryAccountableParty",
            nsmap=frd_namespaces,
        )
        delivery_accountable_party.text = self.srcdocdata["delivery_accountable_party"]

        # add bro id of the formation resistance dossier
        bro_id = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "broId",
            nsmap=frd_namespaces,
        )
        bro_id.text = self.srcdocdata["bro_id"]
        
        # add quality regime
        quality_regime = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "qualityRegime",
            nsmap=frd_namespaces,
        )
        quality_regime.text = self.srcdocdata["quality_regime"]
        
        correction_reason = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "correctionReason",
            nsmap=frd_namespaces,
        )
        correction_reason.text = self.srcdocdata["correction_reason"]

    @abstractmethod
    def create_sourcedocument(self):
        pass



class FrdStartregistrationTool(FRDRegistrationTool):
    """
    Handles all actions for the delivery of FRD Data to the BRO.
    Consists of methods to generate, validate and send FRD XML documents.
    """
    def setup_xml_tree(self):
        """
        Sets up the basis of a startregistration xml file
        """
        # Setup file
        self.xml_tree = etree.Element(
                "registrationRequest",
                nsmap=frd_namespaces,
            )
        
        self.xml_tree.set(
            "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
            "http://www.broservices.nl/xsd/isfrd/1.0 ../../XSD/isfrd-messages.xsd",
        )

        # add request
        request_reference = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "requestReference",
            nsmap=frd_namespaces,
        )
        request_reference.text = self.srcdocdata["request_reference"]

        # add delivery accountable party
        delivery_accountable_party = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "deliveryAccountableParty",
            nsmap=frd_namespaces,
        )
        delivery_accountable_party.text = self.srcdocdata["delivery_accountable_party"]

        # add quality regime
        quality_regime = etree.SubElement(
            self.xml_tree,
            ("{%s}" % frd_namespaces["brocom"]) + "qualityRegime",
            nsmap=frd_namespaces,
        )
        quality_regime.text = self.srcdocdata["quality_regime"]


    def create_sourcedocument(self):
        id_count = 1
        self.source_document = etree.Element("sourceDocument", nsmap=frd_nsmap)

        # Create Startregistration element
        frd_startregistration = etree.Element(
            "{http://www.broservices.nl/xsd/isfrd/1.0}FRD_StartRegistration"
        )
        frd_startregistration.set("{http://www.opengis.net/gml/3.2}id", f"id_000{id_count}")
        id_count += 1

        
        # Add object id accountable party subelement to frd_startregistration
        object_id_accountable_party = etree.SubElement(
            frd_startregistration,
            "{http://www.broservices.nl/xsd/isfrd/1.0}objectIdAccountableParty"    
        )
        object_id_accountable_party.text = self.srcdocdata["object_id_accountable_party"]
        

        # Check if gmn is present in srcdocdata. If so, create element
        if self.srcdocdata["gmn_bro_id"] is not None:
            grounwater_monitoring_net = etree.Element("groundwaterMonitoringNet")
            gmn_element = etree.SubElement(
                grounwater_monitoring_net,
                "{http://www.broservices.nl/xsd/isfrd/1.0}GroundwaterMonitoringNet",
            )
            gmn_element.set("{http://www.opengis.net/gml/3.2}id", f"id_000{id_count}")
            id_count += 1
            gmn_bro_id = etree.SubElement(gmn_element, "{http://www.broservices.nl/xsd/isfrd/1.0}broId")
            gmn_bro_id.text = self.srcdocdata["gmn_bro_id"]
            frd_startregistration.append(grounwater_monitoring_net)

        # add grounwaterMonitoringTube
        grounwater_monitoring_tube = etree.Element("groundwaterMonitoringTube")
        tube_element = etree.SubElement(
            grounwater_monitoring_tube,
            "{http://www.broservices.nl/xsd/frdcommon/1.0}MonitoringTube",
        )
        tube_element.set("{http://www.opengis.net/gml/3.2}id", f"id_000{id_count}")
        id_count += 1

        tube_bro_id = etree.SubElement(tube_element, "{http://www.broservices.nl/xsd/frdcommon/1.0}broId")
        tube_bro_id.text = self.srcdocdata["gmw_bro_id"]
        
        tube_number = etree.SubElement(tube_element, "{http://www.broservices.nl/xsd/frdcommon/1.0}tubeNumber")
        tube_number.text = self.srcdocdata["gmw_tube_number"]

        frd_startregistration.append(grounwater_monitoring_tube)

        # Add startregistration to sourcedocs
        self.source_document.append(frd_startregistration)


class ConfigurationRegistrationTool(FRDRegistrationTool):
    """
    Sets up the xml file for the measurement configuration registrations of the FRD domain
    """
    def create_sourcedocument(self):
        id_count = 1
        self.source_document = etree.Element("sourceDocument", nsmap=frd_nsmap)

        # Create Main element
        gem_measurement_configuration  = etree.Element(
            "FRD_GEM_MeasurementConfiguration"
        )
        gem_measurement_configuration.set("{http://www.opengis.net/gml/3.2}id", f"id_000{id_count}")
        
        id_count += 1

        for configuration in self.srcdocdata["measurement_configurations"]:
            gem_measurement_configuration.append(
                constructables.measurement_configuration(configuration)
            )
        
        self.source_document.append(gem_measurement_configuration)
        print(self.source_document)
  
class GeoOhmMeasuementRegistrationTool(FRDRegistrationTool):
    """
    Sets up the xml file for the geo-ohm measurement configuration registrations of the FRD domain
    """
    def create_sourcedocument(self):
        id_count = 1
        self.source_document = etree.Element("sourceDocument", nsmap=frd_nsmap)

        # Create Main element
        gem_measurement  = etree.Element(
            "FRD_GEM_Measurement"
        )
        gem_measurement.set("{http://www.opengis.net/gml/3.2}id", f"id_000{id_count}")
        id_count += 1

        
        # Initialize related Geo Electric Measurement
        related_geo_electric_measurement = etree.SubElement(
            gem_measurement,
            "relatedGeoElectricMeasurement"    
        )

        # Generate actual measurement element
        geo_electric_measurement = etree.SubElement(
            related_geo_electric_measurement,
            "{http://www.broservices.nl/xsd/frdcommon/1.0}GeoElectricMeasurement"
        )
        geo_electric_measurement.set("{http://www.opengis.net/gml/3.2}id", f"id_000{id_count}")
        id_count += 1

        # Define measurement date
        measurement_date = etree.SubElement(
            geo_electric_measurement,
            "{http://www.broservices.nl/xsd/frdcommon/1.0}measurementDate",
        )
        measurement_date.text = self.srcdocdata["measurement_date"]


        # Define measurement operator element
        measurement_operator = etree.SubElement(
            geo_electric_measurement,
            "{http://www.broservices.nl/xsd/frdcommon/1.0}measurementOperator",
        )

        # Define measurement operator kvk
        measurement_operator_kvk = etree.SubElement(
            measurement_operator,
            "{http://www.broservices.nl/xsd/brocommon/3.0}chamberOfCommerceNumber"
        )
        measurement_operator_kvk.text = self.srcdocdata["chamberOfCommerceNumber"]

        # Define determination procedure
        determination_procedure = etree.SubElement(
            geo_electric_measurement,
            "{http://www.broservices.nl/xsd/frdcommon/1.0}determinationProcedure",
        )

        # Define evaluation procedure
        evaluation_procedure = etree.SubElement(
            geo_electric_measurement,
            "{http://www.broservices.nl/xsd/frdcommon/1.0}evaluationProcedure",
        )

        for measure in self.srcdocdata["geoOhmMeasure"]:
            measure_element = constructables.measure(measure)
            geo_electric_measurement.append(measure_element)
