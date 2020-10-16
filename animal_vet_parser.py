import json
import os
import re
from bs4 import BeautifulSoup
import unicodedata
import csv
import time

print('import success')

# Define variables - YOU CAN CUSTOMIZE IT DEPENDS ON YOUR NEEDS
input_jsonfile = os.getcwd() + '\\animalandveterinary-event-0001-of-0001.json' # THE JSON FILE
output_filename = 'Animal and Veterinary Output.csv' # THE OUTPUT FILENAME

def clean_string(string):
    string = string.replace('\"', '\'\'').replace('\r', ' ').replace('\n', ' ')
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
    string = string.decode('ascii')

    return string
    
def main(json_data):
    print('Num of JSON results: ' + str(len(json_data['results'])))

    for x, data in enumerate(json_data['results']):
        # # For testing
        # if x == 5:
        #     break
        
        print('============= Index ' + str(x) + ' ============= ')

        ## ANIMAL
        try:
            animal = data['animal']
            str_animal = {'animal_' + k: v for k, v in animal.items()}
        except:
            animal = '-'
            str_animal = '-'
        print('Animal: ' + str(str_animal))

        # Age
        try:
            animal_age = animal['age']
        except:
            animal_age = '-'
        print('Animal | Age: ' + str(animal_age))

        # Age - Max
        try:
            animal_age_max = animal_age['max']
        except:
            animal_age_max = '-'
        print('Animal | Age - Max: ' + str(animal_age_max))

        # Age - Min
        try:
            animal_age_min = animal_age['min']
        except:
            animal_age_min = '-'
        print('Animal | Age - Min: ' + str(animal_age_min))

        # Age - Qualifier
        try:
            animal_age_qualifier = animal_age['qualifier']
        except:
            animal_age_qualifier = '-'
        print('Animal | Age - Qualifier: ' + str(animal_age_qualifier))

        # Age - Unit
        try:
            animal_age_unit = animal_age['unit']
        except:
            animal_age_unit = '-'
        print('Animal | Age - Unit: ' + str(animal_age_unit))

        # Breed
        try:
            animal_breed = animal['breed']
        except:
            animal_breed = '-'
        print('Animal | Breed: ' + str(animal_breed))

        # Breed - is_crossbred
        try:
            animal_breed_is_crossbred = animal_breed['is_crossbred']
        except:
            animal_breed_is_crossbred = '-'
        print('Animal | Breed - is_crossbred: ' + str(animal_breed_is_crossbred))

        # Breed - breed_component
        try:
            animal_breed_component = animal_breed['breed_component']
            try:
                animal_breed_component = str(animal_breed_component).replace('[', '')
                animal_breed_component = str(animal_breed_component).replace(']', '')
                animal_breed_component = str(animal_breed_component).replace('\'', '')
            except:
                pass
        except:
            animal_breed_component = '-'
        print('Animal | Breed - breed_component: ' + str(animal_breed_component))

        # Female animal physiological status
        try:
            animal_female_animal_physiological_status = animal['female_animal_physiological_status']
        except:
            animal_female_animal_physiological_status = '-'
        print('Animal | Female animal physiological status: ' + str(animal_female_animal_physiological_status))
        
        # Gender
        try:
            animal_gender = animal['gender']
        except:
            animal_gender = '-'
        print('Animal | Gender: ' + str(animal_gender))

        # Reproductive status
        try:
            animal_reproductive_status = animal['reproductive_status']
        except:
            animal_reproductive_status = '-'
        print('Animal | Reproductive status: ' + str(animal_reproductive_status))

        # Species
        try:
            animal_species = animal['species']
        except:
            animal_species = '-'
        print('Animal | Species: ' + str(animal_species))

        # Weight !
        try:
            animal_weight = animal['weight']
        except:
            animal_weight = '-'
        print('Animal | Weight: ' + str(animal_weight))

        # Weight - Max
        try:
            animal_weight_max = animal_weight['max']
        except:
            animal_weight_max = '-'
        print('Animal | Weight - Max: ' + str(animal_weight_max))

        # Weight - Min
        try:
            animal_weight_min = animal_weight['min']
        except:
            animal_weight_min = '-'
        print('Animal | Weight - Min: ' + str(animal_weight_min))

        # Weight - Qualifier
        try:
            animal_weight_qualifier = animal_weight['qualifier']
        except:
            animal_weight_qualifier = '-'
        print('Animal | Weight - Qualifier: ' + str(animal_weight_qualifier))

        # Weight - Unit
        try:
            animal_weight_unit = animal_weight['unit']
        except:
            animal_weight_unit = '-'
        print('Animal | Weight - Unit: ' + str(animal_weight_unit))

        #####################################################

        ## DRUG ## ADA BANYAK
        try:
            drug = data['drug'][0]
            str_drug = {'drug_' + k: v for k, v in drug.items()}
        except:
            drug = '-'
            str_drug = '-'
        print('Drug: ' + str(str_drug))

        # Active Ingredients ! ## ADA BANYAK
        try:
            drug_active_ingredients = drug['active_ingredients'][0]
        except:
            drug_active_ingredients = '-'
        print('Drug | Active ingredients: ' + str(drug_active_ingredients))

        # Active Ingredients - Name ## ADA BANYAK 
        try:
            drug_active_ingredients_name = drug_active_ingredients['name']
        except:
            drug_active_ingredients_name = '-'
        print('Drug | Active ingredients - Name: ' + str(drug_active_ingredients_name))

        # Administered by
        try:
            drug_administered_by = drug['administered_by']
        except:
            drug_administered_by = '-'
        print('Drug | Administered by: ' + str(drug_administered_by))

        # Abated after stopping drug
        try:
            drug_ae_abated_after_stopping_drug = drug['ae_abated_after_stopping_drug']
        except:
            drug_ae_abated_after_stopping_drug = '-'
        print('Drug | Abated after stopping drug: ' + str(drug_ae_abated_after_stopping_drug))

        # Reappeared after resuming drug
        try:
            drug_ae_reappeared_after_resuming_drug = drug['ae_reappeared_after_resuming_drug']
        except:
            drug_ae_reappeared_after_resuming_drug = '-'
        print('Drug | Reappeared after resuming drug: ' + str(drug_ae_reappeared_after_resuming_drug))

        # ATC Vet code
        try:
            drug_atc_vet_code = drug['atc_vet_code']
        except:
            drug_atc_vet_code = '-'
        print('Drug | ATC Vet code: ' + str(drug_atc_vet_code))

        # Brand name
        try:
            drug_brand_name = drug['brand_name']
        except:
            drug_brand_name = '-'
        print('Drug | Brand name: ' + str(drug_brand_name))

        # Dosage form
        try:
            drug_dosage_form = drug['dosage_form']
        except:
            drug_dosage_form = '-'
        print('Drug | Dosage form: ' + str(drug_dosage_form))

        # First exposure date
        try:
            drug_first_exposure_date = drug['first_exposure_date']
        except:
            drug_first_exposure_date = '-'
        print('Drug | First exposure date: ' + str(drug_first_exposure_date))

        # Frequency of administration
        try:
            drug_frequency_of_administration = drug['frequency_of_administration']
        except:
            drug_frequency_of_administration = '-'
        print('Drug | Frequency of administration: ' + str(drug_frequency_of_administration))

        # Frequency of administration - Unit
        try:
            drug_frequency_of_administration_unit = drug_frequency_of_administration['unit']
        except:
            drug_frequency_of_administration_unit = '-'
        print('Drug | Frequency of administration - Unit: ' + str(drug_frequency_of_administration_unit))

        # Frequency of administration - Value
        try:
            drug_frequency_of_administration_value = drug_frequency_of_administration['value']
        except:
            drug_frequency_of_administration_value = '-'
        print('Drug | Frequency of administration - Value: ' + str(drug_frequency_of_administration_value))

        # Last exposure date
        try:
            drug_last_exposure_date = drug['last_exposure_date']
        except:
            drug_last_exposure_date = '-'
        print('Drug | Last exposure date: ' + str(drug_last_exposure_date))

        # Lot expiration
        try:
            drug_lot_expiration = drug['lot_expiration']
        except:
            drug_lot_expiration = '-'
        print('Drug | Lot expiration: ' + str(drug_lot_expiration))

        # Lot number
        try:
            drug_lot_number = drug['lot_number']
        except:
            drug_lot_number = '-'
        print('Drug | Lot number: ' + str(drug_lot_number))

        # Manufacturer
        try:
            drug_manufacturer = drug['manufacturer']
        except:
            drug_manufacturer = '-'
        print('Drug | Manufacturer: ' + str(drug_manufacturer))

        # Manufacturer - name
        try:
            drug_manufacturer_name = drug_manufacturer['name']
        except:
            drug_manufacturer_name = '-'
        print('Drug | Manufacturer - Name: ' + str(drug_manufacturer_name))

        # Manufacturer - Registration number
        try:
            drug_manufacturer_registration_number = drug_manufacturer['registration_number']
        except:
            drug_manufacturer_registration_number = '-'
        print('Drug | Manufacturer - Registration number: ' + str(drug_manufacturer_registration_number))

        # Manufacturer date
        try:
            drug_manufacturing_date = drug['manufacturing_date']
        except:
            drug_manufacturing_date = '-'
        print('Drug | Manufacturer date: ' + str(drug_manufacturing_date))

        # Number of defective items
        try:
            drug_number_of_defective_items = drug['number_of_defective_items']
        except:
            drug_number_of_defective_items = '-'
        print('Drug | Number of defective items: ' + str(drug_number_of_defective_items))

        # Number of items returned
        try:
            drug_number_of_items_returned = drug['number_of_items_returned']
        except:
            drug_number_of_items_returned = '-'
        print('Drug | Number of items returned: ' + str(drug_number_of_items_returned))

        # Off label use
        try:
            drug_off_label_use = drug['off_label_use']
        except:
            drug_off_label_use = '-'
        print('Drug | Off label use: ' + str(drug_off_label_use))

        # Previous ae to drug
        try:
            drug_previous_ae_to_drug = drug['previous_ae_to_drug']
        except:
            drug_previous_ae_to_drug = '-'
        print('Drug | Previous ae to drug: ' + str(drug_previous_ae_to_drug))

        # Previous exposure to drug
        try:
            drug_previous_exposure_to_drug = drug['previous_exposure_to_drug']
        except:
            drug_previous_exposure_to_drug = '-'
        print('Drug | Previous exposure to drug: ' + str(drug_previous_exposure_to_drug))

        # Product NDC
        try:
            drug_product_ndc = drug['product_ndc']
        except:
            drug_product_ndc = '-'
        print('Drug | Product NDC: ' + str(drug_product_ndc))

        # Route
        try:
            drug_route = drug['route']
        except:
            drug_route = '-'
        print('Drug | Route: ' + str(drug_route))

        # Used according to label
        try:
            drug_used_according_to_label = drug['used_according_to_label']
        except:
            drug_used_according_to_label = '-'
        print('Drug | Used according to label: ' + str(drug_used_according_to_label))

        #####################################################

        ## DURATION
        try:
            duration = data['duration']
        except:
            duration = '-'
        print('Duration: ' + str(duration))

        # Duration - Unit
        try:
            duration_unit = duration['unit']
        except:
            duration_unit = '-'
        print('Duration | Unit: ' + str(duration_unit))

        # Duration - Value
        try:
            duration_value = duration['value']
        except:
            duration_value = '-'
        print('Duration | Value: ' + str(duration_value))

        #####################################################

        ## HEALTH ASSESSMENT PRIOR TO EXPOSURE
        try:
            health_assessment_prior_to_exposure = data['health_assessment_prior_to_exposure']
            str_health_assessment_prior_to_exposure = {'health_assessment_prior_to_exposure_' + k: v for k, v in health_assessment_prior_to_exposure.items()}
        except:
            health_assessment_prior_to_exposure = '-'
            str_health_assessment_prior_to_exposure = '-'
        print('Health Assessment prior to exposure: ' + str(str_health_assessment_prior_to_exposure))

        # Health Assessment prior to exposure - Assessed by
        try:
            health_assessment_prior_to_exposure_assessed_by = health_assessment_prior_to_exposure['assessed_by']
        except:
            health_assessment_prior_to_exposure_assessed_by = '-'
        print('Health Assessment prior to exposure | Assessed by: ' + str(health_assessment_prior_to_exposure_assessed_by))

        # Health Assessment prior to exposure - Condition
        try:
            health_assessment_prior_to_exposure_condition = health_assessment_prior_to_exposure['condition']
        except:
            health_assessment_prior_to_exposure_condition = '-'
        print('Health Assessment prior to exposure | Condition: ' + str(health_assessment_prior_to_exposure_condition))

        #####################################################

        # NUMBER OF ANIMALS AFFECTED
        try:
            number_of_animals_affected = data['number_of_animals_affected']
        except:
            number_of_animals_affected = '-'
        print('Number of animas affected: ' + str(number_of_animals_affected))

        #####################################################

        # NUMBER OF ANIMALS TREATED
        try:
            number_of_animals_treated = data['number_of_animals_treated']
        except:
            number_of_animals_treated = '-'
        print('Number of animas treated: ' + str(number_of_animals_treated))

        #####################################################

        # ONSEN DATE
        try:
            onset_date = data['onset_date']
        except:
            onset_date = '-'
        print('Onsen date: ' + str(onset_date))

        #####################################################

        # ORIGINAL RECEIVE DATE
        try:
            original_receive_date = data['original_receive_date']
        except:
            original_receive_date = '-'
        print('Original receive date: ' + str(original_receive_date))

        #####################################################

        # OUTCOME ## ADA BANYAK
        try:
            outcome = data['outcome'][0]
            str_outcome = {'outcome_' + k: v for k, v in outcome.items()}
        except:
            outcome = '-'
            str_outcome = '-'
        print('Outcome: ' + str(str_outcome))

        # Outcome - Medical Status
        try:
            # outcome_medical_status = []
            # for ea_outcome_medical_status in outcome:
            #     outcome_medical_status.append(ea_outcome_medical_status['medical_status'])
            # outcome_medical_status = str(outcome_medical_status).replace('[', '')
            # outcome_medical_status = str(outcome_medical_status).replace(']', '')
            # outcome_medical_status = str(outcome_medical_status).replace('\'', '')
            outcome_medical_status = outcome['medical_status']
        except:
            outcome_medical_status = '-'
        print('Outcome | Medical Status: ' + str(outcome_medical_status))

        # Outcome - Number of animals affected
        try:
            # outcome_number_of_animals_affected = []
            # for ea_outcome_number_of_animals_affected in outcome:
            #     outcome_number_of_animals_affected.append(ea_outcome_number_of_animals_affected['number_of_animals_affected'])
            # outcome_number_of_animals_affected = str(outcome_number_of_animals_affected).replace('[', '')
            # outcome_number_of_animals_affected = str(outcome_number_of_animals_affected).replace(']', '')
            # outcome_number_of_animals_affected = str(outcome_number_of_animals_affected).replace('\'', '')
            outcome_number_of_animals_affected = outcome['number_of_animals_affected']
        except:
            outcome_number_of_animals_affected = '-'
        print('Outcome | Number of animals affected: ' + str(outcome_number_of_animals_affected))

        #####################################################

        # PRIMARY REPORTER
        try:
            primary_reporter = data['primary_reporter']
        except:
            primary_reporter = '-'
        print('Primary reporter: ' + str(primary_reporter))

        # #####################################################

        # REACTION ## ADA BANYAK
        try:
            reaction = data['reaction'][0]
            str_reaction = {'reaction_' + k: v for k, v in reaction.items()}
        except:
            reaction = '-'
            str_reaction = '-'
        print('Reaction: ' + str(str_reaction))

        # Reaction - Accuracy
        try:
            # reaction_accuracy = []
            # for ea_reaction_accuracy in reaction:
            #     reaction_accuracy.append(ea_reaction_accuracy['accuracy'])
            # reaction_accuracy = str(reaction_accuracy).replace('[', '')
            # reaction_accuracy = str(reaction_accuracy).replace(']', '')
            # reaction_accuracy = str(reaction_accuracy).replace('\'', '')
            reaction_accuracy = reaction['accuracy']
        except:
            reaction_accuracy = '-'
        print('Reaction | Accuracy: ' + str(reaction_accuracy))

        # Reaction - Number of animals affected
        try:
            # reaction_number_of_animals_affected = []
            # for ea_reaction_number_of_animals_affected in reaction:
            #     reaction_number_of_animals_affected.append(ea_reaction_number_of_animals_affected['number_of_animals_affected'])
            # reaction_number_of_animals_affected = str(reaction_number_of_animals_affected).replace('[', '')
            # reaction_number_of_animals_affected = str(reaction_number_of_animals_affected).replace(']', '')
            # reaction_number_of_animals_affected = str(reaction_number_of_animals_affected).replace('\'', '')
            reaction_number_of_animals_affected = reaction['number_of_animals_affected']
        except:
            reaction_number_of_animals_affected = '-'
        print('Reaction | Number of animals affected: ' + str(reaction_number_of_animals_affected))

        # Reaction - Veddra term code
        try:
            # reaction_veddra_term_code = []
            # for ea_reaction_veddra_term_code in reaction:
            #     reaction_veddra_term_code.append(ea_reaction_veddra_term_code['veddra_term_code'])
            # reaction_veddra_term_code = str(reaction_veddra_term_code).replace('[', '')
            # reaction_veddra_term_code = str(reaction_veddra_term_code).replace(']', '')
            # reaction_veddra_term_code = str(reaction_veddra_term_code).replace('\'', '')
            reaction_veddra_term_code = reaction['veddra_term_code']
        except:
            reaction_veddra_term_code = '-'
        print('Reaction | Veddra term code: ' + str(reaction_veddra_term_code))

        # Reaction - Veddra term name
        try:
            # reaction_veddra_term_name = []
            # for ea_reaction_veddra_term_name in reaction:
            #     reaction_veddra_term_name.append(ea_reaction_veddra_term_name['veddra_term_name'])
            # reaction_veddra_term_name = str(reaction_veddra_term_name).replace('[', '')
            # reaction_veddra_term_name = str(reaction_veddra_term_name).replace(']', '')
            # reaction_veddra_term_name = str(reaction_veddra_term_name).replace('\'', '')
            reaction_veddra_term_name = reaction['veddra_term_name']
        except:
            reaction_veddra_term_name = '-'
        print('Reaction | Veddra term name: ' + str(reaction_veddra_term_name))

        # Reaction - Veddra version
        try:
            # reaction_veddra_version = []
            # for ea_reaction_veddra_version in reaction:
            #     reaction_veddra_version.append(ea_reaction_veddra_version['veddra_version'])
            # reaction_veddra_version = str(reaction_veddra_version).replace('[', '')
            # reaction_veddra_version = str(reaction_veddra_version).replace(']', '')
            # reaction_veddra_version = str(reaction_veddra_version).replace('\'', '')
            reaction_veddra_version = reaction['veddra_version']
        except:
            reaction_veddra_version = '-'
        print('Reaction | Veddra version: ' + str(reaction_veddra_version))

        #####################################################

        # RECEIVER
        try:
            receiver = data['receiver']
            str_receiver = {'receiver_' + k: v for k, v in receiver.items()}
        except:
            receiver = '-'
            str_receiver = '-'
        print('Receiver: ' + str(str_receiver))

        # Receiver - City
        try:
            receiver_city = receiver['city']
        except:
            receiver_city = '-'
        print('Receiver | City: ' + str(receiver_city))

        # Receiver - Country
        try:
            receiver_country = receiver['country']
        except:
            receiver_country = '-'
        print('Receiver | Country: ' + str(receiver_country))

        # Receiver - Organization
        try:
            receiver_organization = receiver['organization']
        except:
            receiver_organization = '-'
        print('Receiver | Organization: ' + str(receiver_organization))

        # Receiver - Postal code
        try:
            receiver_postal_code = receiver['postal_code']
        except:
            receiver_postal_code = '-'
        print('Receiver | Postal code: ' + str(receiver_postal_code))

        # Receiver - State
        try:
            receiver_state = receiver['state']
        except:
            receiver_state = '-'
        print('Receiver | State: ' + str(receiver_state))

        # Receiver - Street address
        try:
            receiver_street_address = receiver['street_address']
        except:
            receiver_street_address = '-'
        print('Receiver | Street address: ' + str(receiver_street_address))

        #####################################################

        # REPORT ID
        try:
            report_id = data['report_id']
        except:
            report_id = '-'
        print('Report ID: ' + str(report_id))

        #####################################################

        # SECONDARY REPORTER
        try:
            secondary_reporter = data['secondary_reporter']
        except:
            secondary_reporter = '-'
        print('Secondary reporter: ' + str(secondary_reporter))

        #####################################################

        # SERIOUS AE
        try:
            serious_ae = data['serious_ae']
        except:
            serious_ae = '-'
        print('Serious ae: ' + str(serious_ae))

        #####################################################

        # TIME BETWEEN EXPOSURE AND ONSET
        try:
            time_between_exposure_and_onset = data['time_between_exposure_and_onset']
        except:
            time_between_exposure_and_onset = '-'
        print('Time between exposure and onset: ' + str(time_between_exposure_and_onset))

        #####################################################

        # TREATED FOR AE
        try:
            treated_for_ae = data['treated_for_ae']
        except:
            treated_for_ae = '-'
        print('Treated for ae: ' + str(treated_for_ae))

        #####################################################

        # TYPE OF INFORMATION
        try:
            type_of_information = data['type_of_information']
        except:
            type_of_information = '-'
        print('Type of information: ' + str(type_of_information))

        #####################################################

        # UNIQUE AER ID NUMBER
        try:
            unique_aer_id_number = data['unique_aer_id_number']
        except:
            unique_aer_id_number = '-'
        print('Unique aer id number: ' + str(unique_aer_id_number))

        #####################################################

        print('DONE')
        print('------------------------------------------------')

        dict_data = {
            'animal': str_animal,
            'age': animal_age,
            'age_max': animal_age_max,
            'age_min': animal_age_min,
            'age_qualifier': animal_age_qualifier,
            'age_unit': animal_age_unit,
            'breed': animal_breed,
            'is_crossbred': animal_breed_is_crossbred,
            'breed_component': animal_breed_component,
            'female_animal_physiologic_status': animal_female_animal_physiological_status,
            'gender': animal_gender,
            'reproductive_status': animal_reproductive_status,
            'species': animal_species,
            'weight': animal_weight,
            'weight_max': animal_weight_max,
            'weight_min': animal_weight_min,
            'weight_qualifier': animal_weight_qualifier,
            'weight_unit': animal_weight_unit,
            'drug': str_drug,
            'active_ingredients': drug_active_ingredients,
            'name': drug_active_ingredients_name,
            'administered_by': drug_administered_by,
            'ae_abated_after_stopping_drug': drug_ae_abated_after_stopping_drug,
            'ae_reappeared_after_resuming_drug': drug_ae_reappeared_after_resuming_drug,
            'atc_vet_code': drug_atc_vet_code,
            'brand_name': drug_brand_name,
            'dosage_form': drug_dosage_form,
            'first_exposure_date': drug_first_exposure_date,
            'frequency_of_administration': drug_frequency_of_administration,
            'frequency_of_administration_unit': drug_frequency_of_administration_unit,
            'frequency_of_administration_value': drug_frequency_of_administration_value,
            'last_exposure_date': drug_last_exposure_date,
            'lot_expiration': drug_lot_expiration,
            'lot_number': drug_lot_number,
            'manufacturer': drug_manufacturer,
            'manufacturer_name': drug_manufacturer_name,
            'registration_number': drug_manufacturer_registration_number,
            'manufacturing_date': drug_manufacturing_date,
            'number_of_defective_items': drug_number_of_defective_items,
            'number_of_items_returned': drug_number_of_items_returned,
            'off_label_use': drug_off_label_use,
            'previous_ae_to_drug': drug_previous_ae_to_drug,
            'previous_exposure_to_drug': drug_previous_exposure_to_drug,
            'product_ndc': drug_product_ndc,
            'route': drug_route,
            'used_according_to_label': drug_used_according_to_label,
            'duration': duration,
            'duration_unit': duration_unit,
            'duration_value': duration_value,
            'health_assessment_prior_to_exposure': str_health_assessment_prior_to_exposure,
            'assessed_by': health_assessment_prior_to_exposure_assessed_by,
            'condition': health_assessment_prior_to_exposure_condition,
            'number_of_animals_affected': number_of_animals_affected,
            'number_of_animals_treated': number_of_animals_treated,
            'onset_date': onset_date,
            'original_receive_date': original_receive_date,
            'outcome': str_outcome,
            'medical_status': outcome_medical_status,
            'outcome_number_of_animals_affected': outcome_number_of_animals_affected,
            'primary_reporter': primary_reporter,
            'reaction': str_reaction,
            'accuracy': reaction_accuracy,
            'reaction_number_of_animals_affected': reaction_number_of_animals_affected,
            'veddra_term_code': reaction_veddra_term_code,
            'veddra_term_name': reaction_veddra_term_name,
            'veddra_version': reaction_veddra_version,
            'receiver': str_receiver,
            'city': receiver_city,
            'country': receiver_country,
            'organization': receiver_organization,
            'postal_code': receiver_postal_code,
            'state': receiver_state,
            'street_address': receiver_street_address,
            'report_id': report_id,
            'secondary_reporter': secondary_reporter,
            'serious_ae': serious_ae,
            'time_between_exposure_and_onset': time_between_exposure_and_onset,
            'treated_for_ae': treated_for_ae,
            'type_of_information': type_of_information,
            'unique_aer_id_number': unique_aer_id_number 
        }
        writer.writerow(dict_data)


if __name__ == '__main__':
    # Define field names
    fieldnames = [
        'animal',
        'age',
        'age_max',
        'age_min',
        'age_qualifier',
        'age_unit',
        'weight_unit',
        'breed',
        'is_crossbred',
        'breed_component',
        'female_animal_physiologic_status',
        'gender',
        'reproductive_status',
        'species',
        'weight',
        'weight_max',
        'weight_min',
        'weight_qualifier',
        'weight_unit',
        'drug',
        'active_ingredients',
        'name',
        'administered_by',
        'ae_abated_after_stopping_drug',
        'ae_reappeared_after_resuming_drug',
        'atc_vet_code',
        'brand_name',
        'dosage_form',
        'first_exposure_date',
        'frequency_of_administration',
        'frequency_of_administration_unit',
        'frequency_of_administration_value',
        'last_exposure_date',
        'lot_expiration',
        'lot_number',
        'manufacturer',
        'manufacturer_name',
        'registration_number',
        'manufacturing_date',
        'number_of_defective_items',
        'number_of_items_returned',
        'off_label_use',
        'previous_ae_to_drug',
        'previous_exposure_to_drug',
        'product_ndc',
        'route',
        'used_according_to_label',
        'duration',
        'duration_unit',
        'duration_value',
        'health_assessment_prior_to_exposure',
        'assessed_by',
        'condition',
        'number_of_animals_affected',
        'number_of_animals_treated',
        'onset_date',
        'original_receive_date',
        'outcome',
        'medical_status',
        'outcome_number_of_animals_affected',
        'primary_reporter',
        'reaction',
        'accuracy',
        'reaction_number_of_animals_affected',
        'veddra_term_code',
        'veddra_term_name',
        'veddra_version',
        'receiver',
        'city',
        'country',
        'organization',
        'postal_code',
        'state',
        'street_address',
        'report_id',
        'secondary_reporter',
        'serious_ae',
        'time_between_exposure_and_onset',
        'treated_for_ae',
        'type_of_information',
        'unique_aer_id_number'
    ]

    with open(output_filename , 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with open(input_jsonfile, 'r', encoding='utf8') as json_file:
            json_data = json.load(json_file, strict=False)

            try:
                main(json_data)  # Call main function
                print('Data saved successfully')
            except Exception as err:
                print('Failed to save')
                print('Error: ' + str(err))
        