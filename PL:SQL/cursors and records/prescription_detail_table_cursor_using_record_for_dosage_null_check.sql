DECLARE
  TYPE PrescriptionRecord IS RECORD (
    PRESCRIPTION_ID PRESCRIPTION_DETAIL.PRESCRIPTION_ID%TYPE,
    MEDICATION_NAME PRESCRIPTION_DETAIL.MEDICATION_NAME%TYPE
  );

  CURSOR cur_prescriptions IS
    SELECT PRESCRIPTION_ID, MEDICATION_NAME
    FROM PRESCRIPTION_DETAIL
    WHERE DOSAGE IS NULL;

  v_prescription PrescriptionRecord;
BEGIN
  OPEN cur_prescriptions;
  LOOP
    FETCH cur_prescriptions INTO v_prescription;
    EXIT WHEN cur_prescriptions%NOTFOUND;

    DBMS_OUTPUT.PUT_LINE('PRESCRIPTION_ID: ' || v_prescription.PRESCRIPTION_ID || ', MEDICATION_NAME: ' || v_prescription.MEDICATION_NAME);
  END LOOP;
  CLOSE cur_prescriptions;
END;
/
