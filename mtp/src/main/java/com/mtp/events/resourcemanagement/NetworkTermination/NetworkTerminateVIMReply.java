/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mtp.events.resourcemanagement.NetworkTermination;

import java.util.ArrayList;
import java.util.HashMap;

public class NetworkTerminateVIMReply {

    private long reqid;
    private long servid; //service identifiers 

    private HashMap<Integer, ArrayList<Boolean>> outcomeListMap; //result of the request
    private HashMap<Integer, ArrayList<Integer>> errorcodeListMap;
    private HashMap<Integer, ArrayList<String>> errormsgListMap; //result of the request

    public NetworkTerminateVIMReply() {
        reqid = 0;
        servid = 0;
        //outcome = false;
        outcomeListMap = new HashMap();
        errorcodeListMap = new HashMap();
        errormsgListMap = new HashMap();
    }

    public NetworkTerminateVIMReply(long reqid, long servid, HashMap<Integer, ArrayList<Boolean>> outcomeListMap, HashMap<Integer, ArrayList<Integer>> errorcodeListMap, HashMap<Integer, ArrayList<String>> errormsgListMap) {
        this.reqid = reqid;
        this.servid = servid;
        this.outcomeListMap = outcomeListMap;
        this.errorcodeListMap = errorcodeListMap;
        this.errormsgListMap = errormsgListMap;
    }

    public long getReqid() {
        return reqid;
    }

    public void setReqid(long reqid) {
        this.reqid = reqid;
    }

    public long getServid() {
        return servid;
    }

    public void setServid(long servid) {
        this.servid = servid;
    }

    public HashMap<Integer, ArrayList<Boolean>> getOutcomeListMap() {
        return outcomeListMap;
    }

    public void setOutcomeListMap(HashMap<Integer, ArrayList<Boolean>> outcomeListMap) {
        this.outcomeListMap = outcomeListMap;
    }

    public HashMap<Integer, ArrayList<Integer>> getErrorcodeListMap() {
        return errorcodeListMap;
    }

    public void setErrorcodeListMap(HashMap<Integer, ArrayList<Integer>> errorcodeListMap) {
        this.errorcodeListMap = errorcodeListMap;
    }

    public HashMap<Integer, ArrayList<String>> getErrormsgListMap() {
        return errormsgListMap;
    }

    public void setErrormsgListMap(HashMap<Integer, ArrayList<String>> errormsgListMap) {
        this.errormsgListMap = errormsgListMap;
    }

}
